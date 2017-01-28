import json

from django.test import Client, TestCase

from products.tests.utils import create_fake_product


class ProductsViewsTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_products_first_page(self):
        for _ in range(15):
            create_fake_product()

        response = self.client.get('/api/v1/products/')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)['data']
        self.assertEqual(len(data), 10)

    def test_products_last_page(self):
        for _ in range(15):
            create_fake_product()

        response = self.client.get('/api/v1/products/', {'page': 2})
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)['data']
        self.assertEqual(len(data), 5)

    def test_products_empty_page(self):
        create_fake_product()

        response = self.client.get('/api/v1/products/', {'page': 2})
        self.assertEqual(response.status_code, 200)

        # There is only on product in the database, which would go into the
        # first page. Second page (and all the further pages) should be empty.
        data = json.loads(response.content)['data']
        self.assertEqual(len(data), 0)

    def test_kids(self):
        create_fake_product()

        response = self.client.get('/api/v1/products/kids/')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'"kids": "1"', response.content)

        create_fake_product(kids=1)

        response = self.client.get('/api/v1/products/kids/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"kids": "1"', response.content)

    def test_by_id_existing(self):
        create_fake_product(id=18)

        response = self.client.get('/api/v1/products/18/')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)['data']
        self.assertEqual(data['id'], '18')

    def test_by_id_missing(self):
        response = self.client.get('/api/v1/products/999/')
        self.assertEqual(response.status_code, 404)

        self.assertIn(b'does not exist', response.content)
