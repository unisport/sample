import json

from django.core.exceptions import ObjectDoesNotExist
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
        self.response = self.client.post(
            '/products/create_product',
            json.dumps({'api_token': self.api_token,
                        'product': self.new_product,
                        }),
            content_type="application/json"
        )
        self.product_id = self.response.json().get('product_id')
        self.client.post(
            'products/delete_product',
            json.dumps({'api_token': self.api_token,
                        'product_id': self.product_id
                        }),
            content_type="application/json")

    def tearDown(self):
        pass

    def test_return_id(self):
        product = Product.objects.get(id=self.product_id)
        self.assertEqual(self.new_product.get('name'), product.name)

    def test_response_status(self):
        self.assertEqual(self.response.status_code, 200)


class DeleteProductTest(TestCase):

    def setUp(self):
        self.api_token = API_TOKEN
        self.new_product = PRODUCT_FIXTURE
        self.client = Client()
        self.create_response = self.client.post(
            '/products/create_product',
            json.dumps({'api_token': self.api_token,
                        'product': self.new_product,
                        }),
            content_type="application/json"
        )
        self.product_id = self.create_response.json().get('product_id')
        self.delete_response = self.client.post(
            '/products/delete_product',
            json.dumps({'api_token': self.api_token,
                        'product_id': self.product_id
                        }),
            content_type="application/json"
        )

    def tearDown(self):
        pass

    def test_response_status(self):
        self.assertEqual(self.delete_response.status_code, 200)

    def test_id_not_exists(self):
        with self.assertRaises(ObjectDoesNotExist) as cm:
            Product.objects.get(id=self.product_id)
        the_exception = cm.exception
        self.assertIsInstance(the_exception, ObjectDoesNotExist)
