import json

from django.test import TestCase, Client

from management.commands import get_fixtures
from products.models import Product

PRODUCT_FIXTURE = {
    "kids": "0",
    "name": "Gavekort",
    "sizes": "One Size",
    "kid_adult": "0",
    "free_porto": "0",
    "price": "0,00",
    "package": "0",
    "delivery": "1-2 dage",
    "url": "https://www.unisport.dk/gavekort/",
    "price_old": "0,00",
    "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/1_maxi_0.jpg",
    "women": "0",
}
API_TOKEN = 'token'

class GetFixturesTest(TestCase):

    def test_json_format(self):
        fixtures = get_fixtures.download_json()
        self.assertIsInstance(fixtures, dict)

    def test_saving_fixtures(self):
        fixtures = get_fixtures.download_json()
        product_data = fixtures.get('products')[0]
        saved_product = get_fixtures.save_product(product_data)
        self.assertIsInstance(saved_product, Product)


class CreateProductTest(TestCase):

    def setUp(self):
        self.api_token = API_TOKEN
        self.new_product = PRODUCT_FIXTURE
        self.client = Client()
        self.response = self.client.get(
            'create_product',
            json.dumps({'api_token': self.api_token,
                        'product': self.new_product
                        })
        )

    def tearDown(self):
        if self.product_id:
            self.client.get(
                'delete_product',
                {'api_token': self.api_token,
                 'product_id': self.product_id
                 })

    def test_return_id(self):
        self.product_id = self.response.json().get('product_id')
        product = Product.objects.get(id=self.product_id)
        self.assertEqual(self.new_product.get('name'), product.name)

    def test_response_status():
        self.assertEqual(self.response.status, 200)


class DeleteProductTest(TestCase):

    def setUp(self):
        self.api_token = API_TOKEN
        self.new_product = PRODUCT_FIXTURE
        self.client = Client()
        self.create_response = self.client.get(
            'create_product',
            json.dumps({'api_token': self.api_token,
                        'product': self.new_product,
                        })
        )
        self.product_id = self.create_response.json().get('product_id')
        self.delete_response = self.client.get(
            'delete_product',
            {'api_token': self.api_token,
             'product_id': self.product_id
             })

    def tearDown(self):
        pass

    def test_response_status(self):
        self.assertEqual(self.delete_response.status, 200)
