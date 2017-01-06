import json
from django.core.urlresolvers import reverse
from django.test import TestCase

from ..models import Product


class TestAppViewTest(TestCase):
    """
    Test view class for test_app module
    """

    def setUp(self):
        self.client.get(reverse('load_data'))

    def test_urls_status(self):
        prod_example = Product.objects.first()
        urls = [reverse('cheapest_10'),
                "%s?page=2" % reverse('cheapest_10'),
                reverse('product', kwargs={'pk': prod_example.id}),
                reverse('kids_products')]
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_products_view(self):
        self.assertNotEqual(Product.objects.count(), 0)
        response = self.client.get(reverse('cheapest_10'))
        products = json.loads(response.content)
        self.assertEqual(len(products['products']),
                         min(Product.objects.count(), 10))
        ordered_products = Product.objects.order_by('price')[0:10]
        self.assertEqual([prod.id for prod in ordered_products],
                         [json.loads(prod)['id']
                          for prod in products['products']])

    def test_product_view(self):
        self.assertNotEqual(Product.objects.count(), 0)
        prod_example = Product.objects.first()
        response = self.client.get(reverse('product',
                                   kwargs={'pk': prod_example.id}))
        product = json.loads(response.content)
        self.assertEqual(prod_example.id, json.loads(product['product'])['id'])

    def kids_products_view(self):
        self.assertNotEqual(Product.objects.count(), 0)
        response = self.client.get(reverse('kids_products'))
        products = json.loads(response.content)
        ordered_products = Product.objects.filter(kids='1').order_by('price')
        self.assertEqual(len(products['products']),
                         len(ordered_products))
        self.assertEqual([prod.id for prod in ordered_products],
                         [json.loads(prod)['id']
                          for prod in products['products']])
