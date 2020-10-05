import unittest
from django.test import Client

class Products_tests(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_products(self):
        # Issue a GET request.
        response = self.client.get('/api/products/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
      
        # Check that the json contains 10 products.
        self.assertEqual(len(response.json()['results']), 10)

    def test_pagination(self):
        # Issue a GET request /?page=2.
        response = self.client.get('/api/products/?page=2')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
      
        # Check that the json contains 10 products.
        self.assertEqual(len(response.json()['results']), 10)