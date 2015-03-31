from __future__ import division, print_function, unicode_literals

import json
from faker import Faker

from django.core.urlresolvers import reverse
from django.test import TestCase

from apps.products.models import Product


fake = Faker()


def create_product(kids='0'):
    return Product.objects.create(
        name=fake.company(),
        kids=kids,
        women='0',
        kid_adult='0',
        package='0',
        free_porto=fake.boolean(),
        delivery='2 days delivery',
        price=fake.pydecimal(positive=True, left_digits=4, right_digits=2),
        price_old=fake.pydecimal(positive=True, left_digits=4, right_digits=2),
        url=fake.uri(),
        img_url=fake.uri(),
    )


class ProductViewTests(TestCase):
    def setUp(self):
        self.response_mime_type = 'application/json'

    def test_kids_products(self):
        """
        test kids products page
        :return:
        """
        # create two products with kids flag 1
        create_product(kids='1')
        create_product(kids='1')
        response = self.client.get(reverse('kids_products'))
        # check if resource reachable
        self.assertEqual(response.status_code, 200)
        # check kids index page length
        response_data = json.loads(response.content)
        self.assertEqual(2, len(response_data.get('data')))

    def test_products(self):
        """
        test products pages
        :return:
        """
        # create two products with kids flag 1
        create_product(kids='0')
        create_product(kids='1')
        product = create_product(kids='0')
        # get products page
        response = self.client.get(reverse('products'))
        # check if resource reachable
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(3, len(response_data.get('data')))
        # get product page
        response = self.client.get(reverse('product', args=(product.id, )))
        response_data = json.loads(response.content)
        # check if resource reachable
        self.assertEqual(response.status_code, 200)
        self.assertIn('price', response_data.get('data').keys())

    def test_json_response(self):
        """
        test response
        :return:
        """
        response = self.client.get(reverse('products'))
        # check if resource reachable
        self.assertEqual(response.status_code, 200)
        # check mime type
        self.assertEqual(response.get('Content-Type', None), self.response_mime_type)
        # check if response contains keys
        response_data = json.loads(response.content)
        self.assertIn('data', response_data.keys())
        self.assertIn('errors', response_data.keys())
        self.assertIn('status', response_data.keys())
        self.assertIsInstance(response_data['data'], list)