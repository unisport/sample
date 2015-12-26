from django.test import TestCase

from management.commands import get_fixtures

from products.models import Product


class GetFixturesTest(TestCase):

    def test_json_format(self):
        fixtures = get_fixtures.download_json()
        self.assertIsInstance(fixtures, dict)

    def test_saving_fixtures(self):
        fixtures = get_fixtures.download_json()
        product_data = fixtures.get('products')[0]
        saved_product = get_fixtures.save_product(product_data)
        self.assertIsInstance(saved_product, Product)
