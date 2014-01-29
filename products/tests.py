"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import json

from django.test import TestCase
from products.models import Product, ProductSize

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class JsonTestCase(TestCase):
    def test_json(self):
        resp = self.client.get('/products/')
        self.assertEqual(resp.status_code, 200)
        products = json.loads(resp.content)
        self.assertEqual(len(products["latest"]), 10)

    def test_pagination(self):
        resp = self.client.get('/products/?page=2')
        self.assertEqual(resp.status_code, 200)
        products = json.loads(resp.content)
        self.assertEqual(len(products["latest"]), 10)

    def test_items(self):
        resp = self.client.get('/products/?page=3&items=5')
        self.assertEqual(resp.status_code, 200)
        products = json.loads(resp.content)
        self.assertEqual(len(products["latest"]), 5)

    def test_category(self):
        resp = self.client.get('/products/kids/')
        self.assertEqual(resp.status_code, 200)
        products = json.loads(resp.content)
        for product in products["latest"]:
            self.assertTrue(product["kids"])


class ProductGetCase(TestCase):
    """ Test getting single product json
    """
    def test_return(self):
        resp = self.client.get('/products/51126/')
        self.assertEqual(resp.status_code, 200)
        product = json.loads(resp.content)
        self.assertEqual(product["id"], "51126")


class ProductsListCase(TestCase):
    """ Test product list
    """
    fixtures = ['products_fixture.json']

    def test_context(self):
        resp = self.client.get('/products/products-list/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[-1].name, "products/index.html")
        self.assertEqual(resp.templates[0].name, "products/products_list.html")
        self.assertTrue('products' in resp.context)


class SizeListCase(TestCase):
    """ Test sizes list
    """
    fixtures = ['products_fixture.json']

    def test_context(self):
        resp = self.client.get('/products/sizes-list/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[-1].name, "products/index.html")
        self.assertEqual(resp.templates[0].name, "products/sizes_list.html")
        self.assertTrue('sizes' in resp.context)


class EditProductCase(TestCase):
    """ Test product_edit
    """
    fixtures = ['products_fixture.json']

    def test_context(self):
        resp = self.client.get('/products/edit-product/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[-1].name, "products/index.html")
        self.assertEqual(resp.templates[0].name, "products/edit_product.html")
        self.assertTrue('form' in resp.context)

    def test_editing(self):
        resp = self.client.get('/products/edit-product/51126/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[-1].name, "products/index.html")
        self.assertEqual(resp.templates[0].name, "products/edit_product.html")
        self.assertTrue('form' in resp.context)
        self.assertTrue('product_id' in resp.context)


class EditSizeCase(TestCase):
    """ Test size edit
    """
    fixtures = ['products_fixture.json']

    def test_context(self):
        resp = self.client.get('/products/edit-size/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[-1].name, "products/index.html")
        self.assertEqual(resp.templates[0].name, "products/edit_size.html")
        self.assertTrue('form' in resp.context)

    def test_editing(self):
        resp = self.client.get('/products/edit-size/5/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[-1].name, "products/index.html")
        self.assertEqual(resp.templates[0].name, "products/edit_size.html")
        self.assertTrue('form' in resp.context)
        self.assertTrue('size_id' in resp.context)