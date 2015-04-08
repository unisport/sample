#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class ProductTests(APITestCase):
    fixtures = ['products.json']

    def test_list_products(self):
        """
        Ensure we can list products.
        """
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Fixture has only 35 products.
        self.assertEqual(response.data['count'], 35)

        # This must be the first page.
        self.assertEqual(response.data['previous'], None)

        # This endpoint must return only 10 products.
        self.assertEqual(len(response.data['results']), 10)

        # We know that this price is the cheapest.
        self.assertEqual(response.data['results'][0]['price'], u'49.00')
        self.assertEqual(response.data['results'][0]['id'], 52)


    def test_list_products_paging(self):
        """
        Ensure we can use paging.
        """
        url = reverse('product-list')
        response = self.client.get(url + '?page=4')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 5)

        # We know the last product.
        self.assertEqual(response.data['results'][4]['id'], 48)
        self.assertEqual(response.data['results'][4]['price'], u'1154.00')

    def test_list_products_kids(self):
        """
        Ensure we can list products with kids=1.
        """
        url = reverse('product-kids')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # We know how many products with kids=1 from fixture.
        self.assertEqual(len(response.data), 13)

        # We know that this price is the cheapest.
        self.assertEqual(response.data[0]['price'], u'79.00')
        self.assertEqual(response.data[0]['id'], 37)

        # We know last product.
        self.assertEqual(response.data[12]['price'], u'349.00')
        self.assertEqual(response.data[12]['id'], 43)

        for product in response.data:
            self.assertEqual(product['kids'], u'1')

    def test_get_product_by_id(self):
        """
        Ensure we can get specific product.
        """
        expected = {
            "id": 50,
            "name": u"Nike - Spilletrøje Precision II Rød/Hvid Børn",
            "price": u"140.00",
            "price_old": u"279.00",
            "delivery": u"1-2 dage",
            "free_porto": u"False",
            "package": u"0",
            "kids": u"1",
            "kid_adult": u"0",
            "women": u"0",
            "sizes": u"140-152 cm/Boys M,152-158 cm/Boys L",
            "url": u"http://www.unisport.dk/fodboldudstyr/nike-spilletrje-precision-ii-rdhvid-brn/131971/",
            "img_url": u"http://s3-eu-west-1.amazonaws.com/product-img/131971_da_mellem.jpg"
        }

        url = reverse('product-id', kwargs={'product_id': 50})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected)

