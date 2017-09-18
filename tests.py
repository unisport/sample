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
            str(order_dict(a, a.keys())), str(order_dict(b, a.keys()))
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
        self.assertDictEqual(
            get("http://127.0.0.1:5000/products").json()[0], product
        )
        self.assertEqual(
            len(get("http://127.0.0.1:5000/products?page=1").json()), 10
        )
        self.assertEqual(
            get("http://127.0.0.1:5000/products?page=4").status_code, 404
        )
    
    def test_kids_products(self):
        self.assertEqual(
           len(get("http://127.0.0.1:5000/products/kids").json()), 4
        )
    
    def test_product_by_id(self):
        a = get("http://127.0.0.1:5000/products/153344").json()
        b = {
            "currency": "DKK",
            "delivery": "1-2 dage",
            "free_porto": "0",
            "id": "153344",
            "image": "https://thumblr-7.unisport.dk/product/153344/7439bfeef274.jpg",
            "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/153344_maxi_0.jpg",
            "is_customizable": "1",
            "kid_adult": "0",
            "kids": "1",
            "name": "Fortuna Düsseldorf Hjemmebanetrøje 2016/17 Børn",
            "online": "1",
            "package": "0",
            "price": "137,00",
            "price_old": "549,00",
            "sizes": "YL/152 cm",
            "url": "https://www.unisport.dk/fodboldtroejer/fortuna-dusseldorf-hjemmebanetrje-201617-brn/153344/",
            "women": "0"
        }
        self.assertDictEqual(
            a, b
        )
        self.assertEqual(
            get("http://127.0.0.1:5000/products/4").status_code, 404
        )

if __name__ == "__main__":
    unittest.main()
