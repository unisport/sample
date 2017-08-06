import unittest
from webservice.views import *
from django.test.client import RequestFactory
import django
django.setup()


class ViewsTestCase(unittest.TestCase):

    def test_json_data(self):

        products = data['products']

        all_products = len(products)
        products_attributes = (len(products[0]))

        self.assertEqual(all_products, 25)
        self.assertEqual(products_attributes, 17)

    def setUp(self):

        self.factory = RequestFactory()

    def test_top_ten_cheapest_view(self):
        request = self.factory.get('products/')
        response = top_ten_cheapest(request)
        self.assertEqual(response.status_code, 200)

    def test_kids_view(self):
        request = self.factory.get('products/kids')
        response = kids(request)
        self.assertEqual(response.status_code, 200)

    def test_choose_product_view(self):
        request = self.factory.get('products/id/')
        response = choose_product(request, 10)
        self.assertEqual(response.status_code, 200)

    def test_paginate(self):
        request = self.factory.get('pagination/')
        response = paginate(request)
        self.assertEqual(response.status_code, 200)

















