import connexion
from swagger_server.models.api_response import ApiResponse
from swagger_server.models.shopping_cart import ShoppingCart
from swagger_server.models.shopping_cart_item import ShoppingCartItem
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
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
    return 'do some magic!'


def checkout(cartId):
    """
    Checkout with the carts contents
    Checks the shopping cart out (submits it to be fulfilled)
    :param cartId: ID of the cart that needs to be fetched
    :type cartId: int

    :rtype: ShoppingCart
    """
    return 'do some magic!'


def get_by_cart_id(cartId):
    """
    Find by cart id
    Returns a shopping cart
    :param cartId: ID of the cart that needs to be fetched
    :type cartId: int

    :rtype: ShoppingCart
    """
    return 'do some magic!'


def get_shopping_cart(customerId):
    """
    Current shopping cart
    Gets the current shopping cart for a given customer, if none exists then one is created
    :param customerId: ID of the customer for the current cart
    :type customerId: int

    :rtype: ShoppingCart
    """
    return 'do some magic!'


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
    return 'do some magic!'
