"""
Basic test cases for the Unisport project.  I trust the SQLite interface, and
have witnessed that the response data in the templates look ok.    
"""

from django.test import TestCase
from django.test.client import Client
from products.models import Item

class ItemTest(TestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        del self.client

    def test_non_existent_object(self):
        response = self.client.get('/products/10000/')
        self.assertEqual(response.status_code, 404)

    def test_invalid_page(self):
        response = self.client.get('/products/', { 'page': 4} )
        self.assertEqual(response.status_code, 404)

    def test_working_pagination(self):
        response = self.client.get('/products/', { 'page' : 3} )
        self.assertEqual(response.status_code, 200)

    def test_kids(self):
        response = self.client.get('/products/kids/')
        self.assertEqual(response.status_code, 200)
