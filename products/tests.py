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
            self.assertEqual(response.status_code, 200, msg='Page is not available: {}'.format(page))

    def test_get_data(self):
        data = get_data(cheapest=True)
        self.assertEqual(type(data), list, msg='Data should be a list of products')
        self.assertTrue(len(data), msg="Data shouldn't be empty")
        # Products should be sorted by price starting with cheapest. Let's create a list of prices
        price_list = [float(p['price'].replace(',', '.')) for p in data]
        self.assertListEqual(price_list, sorted(price_list), msg='Products are not sorted by price')

    def test_products_pages(self):
        pages = ('/products/', '/products/?page=2')
        for page in pages:
            response = self.client.get(page)
            self.assertEqual(response.status_code, 200, msg='Page is not available: {}'.format(page))
            data_on_page = json.loads(response.content)
            # Should return exactly 10 products. Don't test ?page=4 and more, data set is less that 50.
            self.assertLessEqual(len(data_on_page), 10, msg='More than 10 products')

    def test_single_product(self):
        page = '/products/111831/'
        response = self.client.get(page)
        data_on_page = json.loads(response.content)
        self.assertEqual(len(data_on_page), 1, msg="Should be only one product on page")
        self.assertEqual('111831', data_on_page[0]['id'], msg="The product should have a id 111831")

    def test_kids_product(self):
        page = '/products/kids/'
        response = self.client.get(page)
        data_on_page = json.loads(response.content)
        for product in data_on_page:
            self.assertEqual(product['kids'], '1', msg="All products should have kids=='1'")