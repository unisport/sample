from django.test import TestCase
from unisample.api.product.plain_models import ProductData
from unisample.api.product.services.product_service import ProductService
from .utils import create_product


class UserMock(object):
    pass


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

    def test_04_create_product(self):
        user = UserMock()
        product_data = self._get_test_product_data()

        result = self.product_service.create_product(user, product_data)
        self.assertEqual(result.name, product_data.name)
        self.assertEqual(result.price, product_data.price)
        self.assertEqual(result.price_old, product_data.price_old)

    def test_05_update_product(self):
        user = UserMock()
        product = create_product('Product name')

        product_data = self._get_test_product_data()
        product_data.name = 'New product name'
        product_data.pk = product.pk

        self.product_service.update_product(user, product_data)
        product = self.product_service.get_product_detail(product.pk)
        self.assertEqual(product.name, product_data.name)

    def test_06_delete_product(self):
        user = UserMock()
        product = create_product('Product name')

        product = self.product_service.get_product_detail(product.pk)
        self.assertIsNotNone(product)

        self.product_service.delete_product(user, product.pk)

        product = self.product_service.get_product_detail(product.pk)
        self.assertIsNone(product)

    def _get_test_product_data(self):
        return ProductData(
            name="Product Name",
            price=209.0,
            price_old=349.0,
            kids=1,
            women=0,
            kid_adult=0,
            delivery="1-2 dage",
            free_porto=True,
            package=0,
            sizes="EU 27\u00bd/US 10\u00bdC",
            img_url="http://s3-eu-west-1.amazonaws.com/product-img/121973_da_mellem.jpg",
            url="http://www.unisport.dk/fodboldstoevler/nike-fc247-elastico-pro-iii-tf-orangesortneon-brn/121973/",
        )
