import unittest

from django.test import TestCase

from rest_framework.test import APIClient

from api.models import Product

client = APIClient()


def setUp(self):
    Product.objects.create(
        id=1,
        name='test',
        price=10000,
        discount_percentage=0,
        image='http://example.com',
        kids=False,
    )
    Product.objects.create(
        id=2,
        name='testkids',
        price=20000,
        discount_percentage=50,
        image='http://example.com',
        kids=True,
    )
    for x in range(10):
        Product.objects.create(name=str(x), price=x, discount_percentage=x, image='http://a.aa', kids=False)


class ProductTestCase(TestCase):
    def setUp(self):
        setUp(self)

    def test_price_dkk(self):
        self.assertEqual(Product.objects.get(name='test').price_dkk(), 100.0)
        self.assertEqual(Product.objects.get(name='testkids').price_dkk(), 200.0)


class ProductAPITestCase(TestCase):
    def setUp(self):
        setUp(self)

    def test_get(self):
        resp = client.get('/products/1/')
        data = resp.json()
        self.assertEqual(data['name'], 'test')

    def test_list_pagination(self):
        resp = client.get('/products/')
        data = resp.json()
        self.assertEqual(data['count'], 12)
        self.assertEqual(len(data['results']), 10)

    def test_create(self):
        resp = client.post('/products/', {
            'name': 'create',
            'price': 15000,
            'discount_percentage': 10,
            'image': 'http://a.aa',
            'kids': False,
        })
        data = resp.json()
        self.assertEqual(data['name'], 'create')
        self.assertEqual(Product.objects.get(name='create').price, 15000)

    def test_edit(self):
        resp = client.put('/products/1/', {
            'name': 'edit',
            'price': 50000,
            'discount_percentage': 20,
            'image': 'http://a.aa',
            'kids': False,
        })
        data = resp.json()
        self.assertEqual(data['name'], 'edit')
        self.assertEqual(Product.objects.get(name='edit').id, 1)

    def test_delete(self):
        resp = client.delete('/products/1/')
        self.assertRaises(Product.DoesNotExist, lambda: Product.objects.get(pk=1))

    def test_list_kids(self):
        resp = client.get('/products/kids/')
        data = resp.json()
        self.assertEqual(data['count'], 1)

