"""
tests.py - Unisport Sample unit testing
"""

import unittest
import json
from money import Money
from requests import get

from utilities import paginate, parse_money, order_dict

class TestUtilities(unittest.TestCase):
    """
    Test the utilities.py module.
    """
    def test_paginate(self):
        """
        Tests the paginate function.
        """
        self.assertEqual(paginate([1, 2, 3, 4, 5, 6], 3), [[1, 2, 3], [4, 5, 6]])
        self.assertEqual(paginate([1, 2, 3, 4, 5, 6, 7], 3), [[1, 2, 3], [4, 5, 6], [7]])
        self.assertEqual(paginate([1, 2, 3, 4], 1), [[1], [2], [3], [4]])
        self.assertEqual(paginate([1, 2, 3, 4, 5, 6], 6), [[1, 2, 3, 4, 5, 6]])
        self.assertEqual(paginate([1, 2, 3, 4, 5, 6], 10), [[1, 2, 3, 4, 5, 6]])
    
    def test_parse_money(self):
        self.assertEqual(parse_money("10.00", "USD"), Money("10", "USD"))
        self.assertEqual(parse_money("10,00", "DKK"), Money("10", "DKK"))
        self.assertEqual(parse_money("0,00", "DKK"), Money("0", "DKK"))
        self.assertEqual(parse_money("0", "CAD"), Money("0", "CAD"))
        self.assertEqual(parse_money("0.15", "CAD"), Money("0.15", "CAD"))
        self.assertEqual(parse_money("0,15", "DKK"), Money("0.15", "DKK"))
        self.assertEqual(parse_money("10.150,15", "DKK"), Money("10150.15", "DKK"))
        self.assertEqual(parse_money("10.150.000,15", "DKK"), Money("10150000.15", "DKK"))
        self.assertEqual(parse_money("10.000.000,15", "DKK"), Money("10000000.15", "DKK"))
        self.assertEqual(parse_money("10,000,000.15", "USD"), Money("10000000.15", "USD"))
    
    def test_order_dict(self):
        a = {
            "foo": "bar",
            "foz": "baz"
        }
        b = {
            "foz": "baz",
            "foo": "bar"
        }
        self.assertNotEqual(str(a), str(b))
        self.assertEqual(a, b)
        self.assertEqual(
            str(order_dict(a, a.keys())),
            str(order_dict(b, a.keys()))
        )

class TestWebService(unittest.TestCase):
    """
    Test the webservice
    """
    def test_products(self):
        product = {
            "is_customizable": "0",
            "delivery": "1-2 dage",
            "kids": "0",
            "name": "Select Nål Protection - Sort",
            "sizes": "One Size",
            "kid_adult": "0",
            "free_porto": "0",
            "image": "https://thumblr-8.unisport.dk/product/157755/8900b1658d61.jpg",
            "package": "0",
            "price": "9,00",
            "url": "https://www.unisport.dk/fodboldudstyr/select-nal-protection-sort/157755/",
            "online": "1",
            "price_old": "9,00",
            "currency": "DKK",
            "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/157755_maxi_0.jpg",
            "id": "157755",
            "women": "0"
        }
        order = [
            "is_customizable",
            "delivery",
            "kids",
            "name",
            "sizes",
            "kid_adult",
            "free_porto",
            "image",
            "package",
            "price",
            "url",
            "online",
            "price_old",
            "currency",
            "img_url",
            "id",
            "women"
        ]
        self.assertEqual(
            order_dict(get("http://127.0.0.1:5000/products").json()[0], product.keys()),
            product
        )
        # self.assertEqual(
        #     [order_dict(p, order) for p in get("http://127.0.0.1:5000/products").json()],
            
        # )

if __name__ == "__main__":
    unittest.main()
