from mock import patch, Mock
import json

from django.core.management import call_command
from django.test import TestCase

from product_api.models import Product


class ImportTests(TestCase):

    @patch('requests.get')
    def test_import(self, mocked_get):
        """
        Ensure we can import products from API.
        """
        example_response = {
            "latest": [
                {"kids": "1", "name": "Nike - Spilletr\u00f8je Precision II R\u00f8d/Hvid B\u00f8rn", "sizes": "140-152 cm/Boys M,152-158 cm/Boys L", "kid_adult": "0", "free_porto": "False", "price": "140,00", "package": "0", "delivery": "1-2 dage", "url": "http://www.unisport.dk/fodboldudstyr/nike-spilletrje-precision-ii-rdhvid-brn/131971/", "price_old": "279,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/131971_da_mellem.jpg", "id": "131971", "women": "0"},
                {"kids": "0", "name": "Nike - Magista Onda IC Hvid/Gr\u00f8n/Sort", "sizes": "EU 38\u00bd/US 6,EU 40\u00bd/US 7\u00bd,EU 41/US 8,EU 42/US 8\u00bd,EU 42\u00bd/US 9,EU 43/US 9\u00bd,EU 44/US 10,EU 44\u00bd/US 10\u00bd,EU 45/US 11,EU 45\u00bd/US 11\u00bd,EU 46/US 12,EU 47/US 12\u00bd,EU 47\u00bd/US 13,EU 48\u00bd/US 14", "kid_adult": "0", "free_porto": "False", "price": "384,00", "package": "0", "delivery": "1-2 dage", "url": "http://www.unisport.dk/fodboldstovler/nike-magista-onda-ic-hvidgrnsort/124850/", "price_old": "549,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/124850_da_mellem.jpg", "id": "124850", "women": "0"},
                {"kids": "1", "name": "Nike - Hypervenom Phelon TF Hvid/Bl\u00e5/Orange B\u00f8rn ", "sizes": "EU 27/US 10C,EU 27\u00bd/US 10\u00bdC,EU 28/US 11C,EU 28\u00bd/US 11\u00bdC,EU 30/US 12\u00bdC,EU 31/US 13C", "kid_adult": "0", "free_porto": "False", "price": "336,00", "package": "0", "delivery": "1-2 dage", "url": "http://www.unisport.dk/fodboldstoevler/nike-hypervenom-phelon-tf-hvidblaorange-brn/124800/", "price_old": "449,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/124800_da_mellem.jpg", "id": "124800", "women": "0"}
        ]}
        mocked_get.return_value = mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps(example_response)

        self.assertEqual(Product.objects.all().count(), 0)

        call_command('import')

        products = Product.objects.all()
        self.assertEqual(products.count(), 3)


