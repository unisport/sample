import unittest
from django.test import TestCase
from django.core.management import call_command
from api.models import Product
import json

class ImportDataTest(TestCase):

    def test_import_command(self):
        call_command('import_data')
        products = Product.objects.all().count()
        self.assertEqual(products, 25)

class APITests(TestCase):
    fixtures = ['products.json']

    def setUp(self):
        self.list_url = '/products/'
        self.kids_url = '/products/kids/'

    def test_list_products(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

        # test if only 10 elements were returned
        content = json.loads(response.content)
        self.assertEqual(len(content), 10)

        # test if the order is correct
        for i in range(len(content)-1):
            self.assertLessEqual(content[i]['price'], content[i+1]['price'])

    def test_pagination(self):
        # test 1st page
        response = self.client.get(self.list_url,{'page': 1})
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(len(content), 10)

        # test 2md page
        response = self.client.get(self.list_url,{'page': 2})
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(len(content), 10)

        # test 3rd page
        response = self.client.get(self.list_url,{'page': 3})
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(len(content), 5)

        # test 4th page
        response = self.client.get(self.list_url,{'page': 4})
        self.assertEqual(response.status_code, 404)

    def test_product_kids(self):
        response = self.client.get(self.kids_url)
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(len(content), 0)
