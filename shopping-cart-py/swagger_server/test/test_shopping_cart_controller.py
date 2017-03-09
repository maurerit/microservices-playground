# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.api_response import ApiResponse
from swagger_server.models.shopping_cart import ShoppingCart
from swagger_server.models.shopping_cart_item import ShoppingCartItem
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestShoppingCartController(BaseTestCase):
    """ ShoppingCartController integration test stubs """

    def test_add_item_to_card(self):
        """
        Test case for add_item_to_card

        Add item to cart
        """
        item = ShoppingCartItem()
        response = self.client.open('//cart/{cartId}'.format(cartId=789),
                                    method='POST',
                                    data=json.dumps(item),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_checkout(self):
        """
        Test case for checkout

        Checkout with the carts contents
        """
        response = self.client.open('//cart/{cartId}'.format(cartId=789),
                                    method='PATCH',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_by_cart_id(self):
        """
        Test case for get_by_cart_id

        Find by cart id
        """
        response = self.client.open('//cart/{cartId}'.format(cartId=789),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_shopping_cart(self):
        """
        Test case for get_shopping_cart

        Current shopping cart
        """
        customerId = 789
        response = self.client.open('//cart',
                                    method='POST',
                                    data=json.dumps(customerId),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_item_quantity(self):
        """
        Test case for update_item_quantity

        Quantity Update
        """
        item = ShoppingCartItem()
        response = self.client.open('//cart/{cartId}/{itemId}'.format(cartId=789, itemId=789),
                                    method='PATCH',
                                    data=json.dumps(item),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
