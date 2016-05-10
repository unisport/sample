#coding: utf-8
from decimal import Decimal
import json
from random import randint
from django.core.urlresolvers import reverse
from django.test import TestCase
from unisport import settings
from unisport.product import models
from unisport.product.test import factories


class TestProduct(TestCase):
    def test_price_ordering(self):
        cheap_product = factories.ProductFactory(price=1)
        expensive_product = factories.ProductFactory(price=250)

        response = self.client.get(
            reverse('products:get_products'),
        )

        data = json.loads(response.content)
        min_price = json.loads(data['products'][0]['price'])
        max_price = json.loads(data['products'][1]['price'])

        self.assertEqual(min_price, cheap_product.price)
        self.assertEqual(max_price, expensive_product.price)

    def test_empty_products_list(self):
        response = self.client.get(
            reverse('products:get_products'),
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['products'], [])

    def test_pagination(self):
        for product_id in xrange(0, settings.ELEMENTS_ON_PAGE*2):
            factories.ProductFactory.create(price=randint(10, 999))

        for page in xrange(1, 2):
            response = self.client.get(
                reverse('products:get_products')+'?page=%s' % page
            )
            data = json.loads(response.content)
            self.assertEqual(len(data['products']), settings.ELEMENTS_ON_PAGE)
            self.assertLess(
                Decimal(data['products'][0]['price']),
                Decimal(data['products'][1]['price'])
            )

    def test_no_valid_page_return_first(self):
        for product_id in xrange(0, settings.ELEMENTS_ON_PAGE*2):
            factories.ProductFactory.create(price=randint(10, 999))

        for page in ['qwerty', '99', '-1', '0']:
            response = self.client.get(
                reverse('products:get_products')+'?page=%s' % page
            )
            data = json.loads(response.content)

            products = models.Product.objects.all().order_by('price')[:settings.ELEMENTS_ON_PAGE].values()
            self.assertEqual(Decimal(data['products'][0]['price']), products[0]['price'])


    def test_product_by_id(self):
        factories.ProductFactory(id=1)
        factories.ProductFactory(id=2)

        response = self.client.get(
            reverse('products:get_product_by_id', kwargs={'product_id': 1})
        )
        data = json.loads(response.content)
        self.assertTrue('product' in data)
        self.assertEqual(data['product']['id'], 1)

    def test_kids_product_filtering(self):
        factories.ProductFactory(kids=0)
        factories.ProductFactory(kids=1)
        factories.ProductFactory(kids=2)

        response = self.client.get(
            reverse('products:get_kids_product')
        )
        data = json.loads(response.content)

        for product in data['products']:
            self.assertEqual(product['kids'], 1)
