import connexion
from swagger_server.models.api_response import ApiResponse
from swagger_server.models.shopping_cart import ShoppingCart
from swagger_server.models.shopping_cart_item import ShoppingCartItem
from datetime import date, datetime
from typing import List, Dict
from six import iteritems


from swagger_server.models.status import ShoppingCartStatus
from swagger_server.models import db
from ..util import deserialize_date, deserialize_datetime



def add_item_to_card(cartId, item):
    """
    Add item to cart
    Adds an item to the cart
    :param cartId: ID of the cart that needs to be fetched
    :type cartId: int
    :param item: Cart Item to be added
    :type item: dict | bytes

    :rtype: ShoppingCart
    """
    if connexion.request.is_json:
        item = ShoppingCartItem.from_dict(connexion.request.get_json())

    db_cart = ShoppingCart.query.filter_by(_shopping_cart_id=cartId).one_or_none()

    if db_cart is None:
        return 404

    item.shopping_cart_id = cartId
    db.session.merge(item)
    db.session.commit()

    return True


def checkout(cartId):
    """
    Checkout with the carts contents
    Checks the shopping cart out (submits it to be fulfilled)
    :param cartId: ID of the cart that needs to be fetched
    :type cartId: int

    :rtype: ShoppingCart
    """
    db_cart = ShoppingCart.query.filter_by(_shopping_cart_id=cartId).one_or_none()
    db_cart.items = get_cart_items(db_cart.shopping_cart_id)

    if db_cart is None:
        return 404

    db_cart.status = ShoppingCartStatus.ORDERED.name
    db.session.merge(db_cart)

    for item in db_cart.items:
        item.status = ShoppingCartStatus.ORDERED.name
        db.session.merge(item)

    db.session.commit()

    return True


def get_by_cart_id(cartId):
    """
    Find by cart id
    Returns a shopping cart
    :param cartId: ID of the cart that needs to be fetched
    :type cartId: int

    :rtype: ShoppingCart
    """

    db_cart = ShoppingCart.query.filter_by(_shopping_cart_id=cartId).one_or_none()

    shopping_cart = initialize_cart(db_cart)

    shopping_cart.items = get_cart_items(shopping_cart.shopping_cart_id)

    return shopping_cart


def get_shopping_cart(customerId):
    """
    Current shopping cart
    Gets the current shopping cart for a given customer, if none exists then one is created
    :param customerId: ID of the customer for the current cart
    :type customerId: int

    :rtype: ShoppingCart
    """
    db_cart = ShoppingCart.query.filter_by(_customer_id=customerId).one_or_none()
    if db_cart is None:
        db_cart = ShoppingCart(customer_id=customerId, status=ShoppingCartStatus.SHOPPING)
        db_cart = db.session.merge(db_cart)
        db.session.commit()

    shopping_cart = initialize_cart(db_cart)

    shopping_cart_items = get_cart_items(shopping_cart.shopping_cart_id)
    shopping_cart.items = shopping_cart_items

    return shopping_cart


def update_item_quantity(cartId, itemId, item):
    """
    Quantity Update
    Update the quantity of an item in a cart
    :param cartId: ID of the cart for the item needing updated
    :type cartId: int
    :param itemId: Item ID in the cart to be updated
    :type itemId: int
    :param item: item
    :type item: dict | bytes

    :rtype: ShoppingCart
    """
    if connexion.request.is_json:
        item = ShoppingCartItem.from_dict(connexion.request.get_json())

    db_item = ShoppingCartItem.query.filter_by(_shopping_cart_id=item.shopping_cart_id, _item_id=item.item_id).one_or_none()

    if db_item is None:
        return 404

    db.session.merge(item)
    db.session.commit()

    return True


def get_cart_items(cartId: int):
    """

    :param cartId: The shopping cart
    :type cartId: int
    :return:
    """
    """
    TODO: I don't like this, SQLAlchemy HAS to be able to play better with swagger or default constructors?  What the
    hell does python even call these?
    """
    db_items = ShoppingCartItem.query.filter_by(_shopping_cart_id=cartId).all()

    shopping_cart_items = []
    for db_item in db_items:
        shopping_cart_items.append(ShoppingCartItem(item_id=db_item.item_id,
                                                    price=db_item.price,
                                                    quantity=db_item.quantity,
                                                    shopping_cart_id=db_item.shopping_cart_id))
    return shopping_cart_items


def initialize_cart(cart: ShoppingCart):
    """
    Initializes the ShoppingCart so that swagger recognizes it.

    :param cart: The shopping cart from the db to __init__
    :type cart: ShoppingCart
    :return:
    """
    shopping_cart = ShoppingCart(shopping_cart_id=cart.shopping_cart_id,
                                 customer_id=cart.customer_id,
                                 status=ShoppingCartStatus[cart.status])
    return shopping_cart