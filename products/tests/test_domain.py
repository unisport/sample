from django.test import TestCase

from products.domain import get_product_by_id, get_products_page
from products.models import Product
from products.tests.utils import create_fake_product


class GetProductsTests(TestCase):

    def test_page_size(self):
        for i in range(1, 15):
            create_fake_product()

        # First page should contain 10 products
        products = get_products_page(page=1, limit=10)
        self.assertEqual(len(products), 10)

        # Second page should contain 4 products
        products = get_products_page(page=1, limit=10)
        self.assertEqual(len(products), 10)

    def test_ordering(self):
        create_fake_product(price=12)
        create_fake_product(price=25)
        create_fake_product(price=48)

        products = get_products_page(page=1, limit=15)

        self.assertEqual(products[0].price, 12)
        self.assertEqual(products[1].price, 25)
        self.assertEqual(products[2].price, 48)

    def test_ordering_inserted_in_different_order(self):
        create_fake_product(price=48)
        create_fake_product(price=12)
        create_fake_product(price=25)

        products = get_products_page(page=1, limit=15)

        # Products should be ordered from cheap to expensive regardless of
        # the order of insertions.
        self.assertEqual(products[0].price, 12)
        self.assertEqual(products[1].price, 25)
        self.assertEqual(products[2].price, 48)

    def test_for_kids(self):
        create_fake_product()
        create_fake_product()
        create_fake_product()
        create_fake_product(name='a toy', kids=True)

        all_products = get_products_page(page=1, limit=15)
        kids_products = get_products_page(page=1, limit=15, for_kids=True)

        self.assertEqual(len(all_products), 4)
        self.assertEqual(len(kids_products), 1)
        self.assertEqual(kids_products[0].name, 'a toy')

    def test_for_kids_when_number_is_zero(self):
        kids_products = get_products_page(page=1, limit=15, for_kids=True)

        self.assertEqual(len(kids_products), 0)

    def test_get_by_id_existing(self):
        create_fake_product(id=5432)
        product = get_product_by_id(5432)
        self.assertEqual(product.id, 5432)

    def test_get_by_id_missing(self):
        with self.assertRaises(Product.DoesNotExist):
            get_product_by_id(9876)
