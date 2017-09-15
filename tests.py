"""
tests.py - Unisport Sample unit testing
"""

import subprocess
import unittest
from money import Money

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

# class TestWebService(unittest.TestCase):
#     """
#     Test the webservice
#     """
#     def __init__(self):
#         super()
#         self.service = subprocess.Popen("exec python main.py", stdout=subprocess.PIPE, shell=True)

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         self.service.kill()

if __name__ == "__main__":
    unittest.main()
