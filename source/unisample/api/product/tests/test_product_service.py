from django.test import TestCase
from unisample.api.product.services.product_service import ProductService
from .utils import create_product


class TestProductService(TestCase):

    product_service = ProductService()

    def test_01_get_cheapest(self):
        result = list(self.product_service.get_cheapest())
        self.assertListEqual(result, [])

        p1 = create_product('Product1', price=50.0)
        p2 = create_product('Product2', price=45.0)
        p3 = create_product('Product3', price=60.0)

        result = list(self.product_service.get_cheapest())
        self.assertListEqual(result, [p2, p1, p3])

    def test_02_get_kids_products(self):
        p1 = create_product('Product1', kids=1)
        p2 = create_product('Product2')
        p3 = create_product('Product3', kids=1)

        result = list(self.product_service.get_kids_products())

        self.assertListEqual(result, [p1, p3])

    def test_03_get_product_detail(self):
        product = create_product('Product1')

        result = self.product_service.get_product_detail(product.pk)

        self.assertEqual(product, result)
