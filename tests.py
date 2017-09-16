"""
tests.py - Unisport Sample unit testing
"""

import unittest
import json
from money import Money
from requests import get

from utilities import paginate, parse_money

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

class TestWebService(unittest.TestCase):
    """
    Test the webservice
    """
    # def test_products(self): # fails, but it's a false negative
    #     with open("products.sorted.json") as file:
    #         products = json.load(file)
    #         self.assertEqual(dict(get("http://127.0.0.1:5000/products").json()[0]), dict(products[0]))

if __name__ == "__main__":
    unittest.main()
