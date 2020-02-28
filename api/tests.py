"""Test cases."""
from django.test import TestCase
from api.importer import import_unisport_data
from django.test import Client
from api.models import Product
from api.serializers import ProductSerializer
import json


class TestProduct(TestCase):
    """Test Product."""

    fixtures = ["unisport.json"]

    def setUp(self):
        """Return base test objects."""
        self.c = Client()
        self.product_api = "/api/products/"

    def test_product_list(self):
        """Test something."""
        result = self.c.get(self.product_api)
        self.assertEqual(result.status_code, 200)

        response_json = result.json()
        self.assertEqual(response_json.get('count'), 40)
        self.assertEqual(len(response_json.get('results')), 10)

    def test_next_page(self):
        result = self.c.get(self.product_api)
        self.assertEqual(result.status_code, 200)

        next_page_result = self.c.get(f"{self.product_api}?page=2")
        response_json = next_page_result.json()
        self.assertIsNotNone(response_json.get('previous'))

    def test_detail_view(self):
        product_id = 168029
        result = self.c.get(f"{self.product_api}{product_id}")
        self.assertEqual(result.status_code, 200)
        response_json = result.json()
        self.assertEqual(response_json.get('id'), product_id)

    def test_put_edit(self):
        product_id = 168029
        product = Product.objects.get(pk=product_id)
        product.price = 211
        product.currency = "EUR"
        product_data = ProductSerializer(instance=product).data

        result = self.c.put(
            f"{self.product_api}{product_id}",
            product_data,
            content_type="application/json"
        )
        response_json = result.json()
        self.assertEqual(result.status_code, 200)
        self.assertEqual(response_json.get('price'), product.price)
        self.assertEqual(response_json.get('currency'), product.currency)
        product.refresh_from_db()
        self.assertEqual(product.price, 211)
        self.assertEqual(product.currency, "EUR")

    def test_patch_edit(self):
        product_id = 168029
        patch_data = {
            "price": 150,
            "currency": "USD"
        }
        result = self.c.patch(
            f"{self.product_api}{product_id}",
            patch_data,
            content_type="application/json"
        )
        response_json = result.json()
        self.assertEqual(result.status_code, 200)
        self.assertEqual(response_json.get('price'), 150)
        self.assertEqual(response_json.get('currency'), "USD")
        product = Product.objects.get(pk=product_id)
        self.assertEqual(product.price, 150)
        self.assertEqual(product.currency, "USD")

    def test_post_new_product(self):
        product_id = 168029
        product = Product.objects.get(pk=product_id)
        product.id = 268029
        product_data = ProductSerializer(instance=product).data
        result = self.c.post(
            f"{self.product_api}",
            product_data,
            content_type="application/json"
        )
        self.assertEqual(result.status_code, 201)
        self.assertEqual(
            Product.objects.all().count(),
            41
        )

    def test_post_duplicate_product(self):
        product_id = 168029
        product = Product.objects.get(pk=product_id)
        product_data = ProductSerializer(instance=product).data
        result = self.c.post(
            f"{self.product_api}",
            product_data,
            content_type="application/json"
        )
        self.assertEqual(result.status_code, 400)

    def test_delete_product(self):
        product_id = 168029
        result = self.c.delete(f"{self.product_api}{product_id}")
        self.assertEqual(result.status_code, 204)
        all_products = Product.objects.all()
        self.assertEqual(all_products.count(), 39)
