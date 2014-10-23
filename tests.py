# To test the application run ./manage.py test
import json

import unittest
from django.test import Client
from products.views import get_data

__author__ = 'Sergey Smirnov <smirnoffs@gmail.com>'


class ProductsTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_status(self):
        # Check if all pages is available
        pages = ('/products/', '/products/?page=2', "/products/111831/", "/products/33/", "/products/kids/")
        for page in pages:
            response = self.client.get(page)
            self.assertEqual(response.status_code, 200)

    def test_get_data(self):
        data = get_data(cheapest=True)
        # Data should be dict type
        self.assertEqual(type(data), dict)
        # data shouldn't be empty
        self.assertTrue(len(data))
        # data should have 'latest' key
        self.assertIn('latest', data)
        # Products should be sorted by price starting with cheapest. Let's create a list of prices
        price_list = [float(p['price'].replace(',', '.')) for p in data['latest']]
        self.assertListEqual(price_list, sorted(price_list))

    def test_products_pages(self):
        pages = ('/products/', '/products/?page=2')
        for page in pages:
            response = self.client.get(page)
            self.assertEqual(response.status_code, 200)
            data_on_page = json.loads(response.content)
            # Should return exactly 10 products. Don't test ?page=4 and more, data set is less that 50.
            self.assertEqual(len(data_on_page), 10)

    def test_single_product(self):
        page = '/products/111831/'
        response = self.client.get(page)
        data_on_page = json.loads(response.content)
        # Should be only one product on page
        self.assertEqual(len(data_on_page), 1)
        # The product should have a right id
        self.assertEqual('111831', data_on_page[0]['id'])

    def test_kids_product(self):
        page = '/products/kids/'
        response = self.client.get(page)
        data_on_page = json.loads(response.content)
        # All products should have kids=='1'
        for product in data_on_page:
            self.assertEqual(product['kids'], '1')