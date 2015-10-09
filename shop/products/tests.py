# -*- encoding: UTF-8 -*-
"""
Propose: Implemented tests for product api
Author: 'yac'
"""

import json
from django.test import TestCase
from models import Product

class ProductTestCase(TestCase):
    """ Product test case """
    def setUp(self):
        """ init test. create product """
        Product.objects.create(name="prod_1", price='120,00')
        Product.objects.create(name="prod_2", price='200,00')
        Product.objects.create(name="prod_3", price='10,00')


    def test_view_get_product(self):
        """ Check order by price """
        res = self.client.get('/products/').content
        res = json.loads(res)
        self.assertEqual(len(res['result']), 3)
        cheapest = ['prod_3', 'prod_1', 'prod_2']
        for ind, prod in enumerate(res['result']):
            self.assertEqual(prod['name'], cheapest[ind])

    def test_view_get_product_by_page(self):
        """ Check products by page """
        res = self.client.get('/products/?page=1').content
        res = json.loads(res)
        self.assertEqual(len(res['result']), 3)

        res = self.client.get('/products/?page=2').content
        res = json.loads(res)
        self.assertEqual(len(res['result']), 0)

    def test_product(self):
        """Check post method """
        data1 = {"kids": 0,
                "name": "",
                "sizes": "One Size",
                "kid_adult": "0",
                "free_porto": "0",
                "price": "200,00",
                "package": "0",
                "delivery": "1-2 dage",
                "url": "https://www.unisport.dk/gavekort/",
                "price_old": "0,00",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/1_maxi_0.jpg",
                "women": "0"}
        # create
        res = self.client.post('/products/', json.dumps(data1), content_type="application/json").content
        res = json.loads(res)
        self.assertEqual(res['errorMessage'], 'Field <name> is required or empty')

        data1['name'] = 'test1'
        res = self.client.post('/products/', json.dumps(data1), content_type="application/json").content
        res = json.loads(res)
        self.assertEqual(res['id'], 4)

        # update
        data1['name'] = 'UPDATE NAME'
        res = self.client.post('/products/4/', json.dumps(data1), content_type="application/json").content
        res = json.loads(res)
        self.assertEqual(res['success'], True)

        res = self.client.get('/products/4/').content
        res = json.loads(res)
        self.assertEqual(res['result']['name'], 'UPDATE NAME')

        # del
        res = self.client.post('/products/4/', {}, content_type="application/json").content
        res = json.loads(res)
        self.assertEqual(res['success'], True)

        res = self.client.get('/products/4/').content
        self.assertEqual(res, '<h1>Not Found</h1><p>The requested URL /products/4/ was not found on this server.</p>')