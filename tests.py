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
        self.detail_url = '/products/%d/'

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

    def test_product_detail(self):
        response = self.client.get(self.detail_url % 1)
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content['name'], 'Gavekort')
        self.assertEqual(content['price'], '0,00')
        self.assertEqual(content['kids'], '0')
        self.assertEqual(content['url'], 'http://www.unisport.dk/gavekort/')

        response = self.client.get(self.detail_url % 107)
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content['delivery'], '1-2 dage')
        self.assertEqual(content['price_old'], '1.099,00')
        self.assertEqual(content['kid_adult'], '1')
        self.assertEqual(content['img_url'], 'http://s3-eu-west-1.amazonaws.com/product-img/107_maxi_0.jpg')

        # product not found
        response = self.client.get(self.detail_url % 2)
        self.assertEqual(response.status_code, 404)

    def test_post(self):
        # valid data
        data = json.dumps({
            "kids": "1",
            "name": "Test",
            "sizes": "One Size",
            "kid_adult": "0",
            "free_porto": "0",
            "price": "0.0",
            "package": "0",
            "delivery": "1-2 dage",
            "url": "http://www.unisport.dk/gavekort/",
            "price_old": "0.0",
            "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/1_maxi_0.jpg",
            "women": "0",
        })
        response = self.client.post(self.list_url, data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        content = json.loads(response.content)
        self.assertEqual(content['status'], 'Created')
        self.assertEqual(content['product']['name'], 'Test')
        test_product = Product.objects.filter(name='Test').count()
        self.assertEqual(test_product, 1)

        # invalid data format
        response = self.client.post(self.list_url, '{fsadf/..}', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        content = json.loads(response.content)
        self.assertEqual(content['status'], 'Invalid format')

        # data with validation errors
        data = json.dumps({
            "kids": "1",
            "name": "Test",
            "sizes": "One Size",
            "kid_adult": "0",
            "free_porto": "0",
            "price": "0.0",
            "package": "0",
            "delivery": "1-2 dage",
            "price_old": "0.0",
            "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/1_maxi_0.jpg",
            "women": "0",
        })
        response = self.client.post(self.list_url, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        content = json.loads(response.content)
        self.assertEqual(content['status'], 'Validation errors')
        self.assertEqual(content['errors']['url'][0], 'This field cannot be blank.')
        self.assertEqual(content['errors']['name'][0], 'Product with this Name already exists.')

        # data with invalid attribute
        data = json.dumps({
            "kids": "1",
            "name": "Test2",
            "description": "Test description",  # no such field on the Product model
            "sizes": "One Size",
            "kid_adult": "0",
            "free_porto": "0",
            "price": "0.0",
            "package": "0",
            "delivery": "1-2 dage",
            "url": "http://www.unisport.dk/gavekort/",
            "price_old": "0.0",
            "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/1_maxi_0.jpg",
            "women": "0",
        })

        response = self.client.post(self.list_url, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        content = json.loads(response.content)
        self.assertEqual(content['status'], 'Invalid attribute')
