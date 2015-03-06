from random import randint
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from unisport import models


class ProductView(TestCase):
    """Single product view page."""

    fixtures = ['test_products.json']

    def setUp(self):
        self.client = Client()

    def test_non_existent(self):
        """Browsing a non-existent product id returns 404."""

        response = self.client.get(
            reverse('product', kwargs={'product_id': 123456})
        )
        self.assertEqual(response.status_code, 404)

    def test_valid_get(self):
        """A valid GET request returns 200 and a single product as the context."""

        expected_fake_id = 131971
        response = self.client.get(
            reverse('product', kwargs={'product_id': expected_fake_id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product.html')
        self.assertEqual(response.context['product'].fake_id, expected_fake_id)
