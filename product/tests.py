# coding=utf-8

import os
import json

from django.conf import settings
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.test.utils import override_settings

from django_dynamic_fixture import G

from product.models import Product, Size
from product.utils import json_to_product


class UtilsTestCase(TestCase):

    def setUp(self):
        curr = os.path.dirname(os.path.dirname(__file__))
        self.data = json.load(open(os.path.join(curr, 'sample.json'), 'r'))

    def test_json_to_product(self):
        p_data = self.data['latest'][0]
        product, created = json_to_product(p_data)

        self.assertTrue(created)

        p_json = product.as_json()
        for key in p_json:
            if key != 'sizes':
                self.assertTrue(key in p_data)
                self.assertTrue(p_json[key], p_data[key])

        self.assertEqual(set(p_json['sizes'].split(',')), set(p_data['sizes'].split(',')))

        # if we import this again
        # no new product should be created
        product, created = json_to_product(p_data)

        self.assertFalse(created)


class ViewTestCase(TestCase):

    def setUp(self):
        self.kids_products = G(Product, kids=1, n=5)
        self.no_kids_products = G(Product, kids=0, n=5)

        self.client = Client()

    def test_products_view(self):
        """
        /products returns the first 10 objects ordered with the cheapest first
        """
        response = self.client.get(reverse('product.views.products'))
        self.assertEqual(response.status_code, 200)

        json_data = json.loads(response.content)
        json_pids = [p['id'] for p in json_data['cheapest']]

        pids = Product.objects.all().order_by('price').values_list('pid', flat=True)[:10]

        self.assertTrue(all([x == y for x,y in zip(json_pids, pids)]))

    def test_products_kids_view(self):
        """
        /products/kids returns the first 10 objects where kids=1 ordered with the cheapest first
        """
        response = self.client.get(reverse('product.views.kids'))
        self.assertEqual(response.status_code, 200)

        json_data = json.loads(response.content)
        json_pids = [p['id'] for p in json_data['cheapest']]

        pids = Product.objects.filter(kids=1).order_by('price').values_list('pid', flat=True)[:10]

        self.assertTrue(all([x == y for x,y in zip(json_pids, pids)]))

    @override_settings(PRODUCTS_PER_PAGE=2)
    def test_products_view_with_paginator(self):
        """
        /products/?page=2 returns the next 10 objects ordered with the cheapest first
        """
        response = self.client.get(reverse('product.views.products') + '?page=2')
        self.assertEqual(response.status_code, 200)

        json_data = json.loads(response.content)
        json_pids = [p['id'] for p in json_data['cheapest']]

        pids = Product.objects.all().order_by('price').values_list('pid', flat=True)\
            [settings.PRODUCTS_PER_PAGE:settings.PRODUCTS_PER_PAGE*2]

        self.assertTrue(all([x == y for x,y in zip(json_pids, pids)]))

    def test_single_view(self):
        """
        /products/?page=2 returns the next 10 objects ordered with the cheapest first
        """
        _pid = self.kids_products[0].pid
        response = self.client.get(reverse('product.views.single_product', args=[_pid]))
        self.assertEqual(response.status_code, 200)

        json_data = json.loads(response.content)

        p = Product.objects.get(pid=_pid)
        self.assertEqual(json_data, p.as_json())
