from django.test import TestCase
from django.urls import reverse
import json
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework import status


PAGE_SIZE = 10


class EmptyProductsIndexViewTest(TestCase):
    """ProductList view tests whet."""

    def test_no_products(self):
        """
        If no product exist, an empty message is displayed
        with NO_CONTENT HTTP status code.
        """
        response = self.client.get(reverse('products:index'))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ProductsIndexViewTest(TestCase):
    """ProductList view tests."""

    fixtures = ['test_products_all.json']

    def test_default_url_request(self):
        """
        Default behaviour is returning the cheapest PAGE_SIZE products
        ordered by ascending price along with an OK HTTP status code.
        """

        response = self.client.get(reverse('products:index'))
        products = response.json()
        prices = [product['price'] for product in products]
        left_products = Product.objects.all()[1 * PAGE_SIZE:]
        for price in prices:
            for product in left_products:
                self.assertTrue(float(price) <= float(product.price))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(products), PAGE_SIZE)
        self.assertEqual(prices, sorted(prices, key=lambda x: float(x)))

    def test_kids_filter(self):
        """
        Returns all products where kids = true ordered by ascending price
        with an OK HTTP status code.
        """

        response = self.client.get(reverse('products:kids'))
        products = response.json()
        prices = [product['price'] for product in products]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(products), 5)
        self.assertEqual(prices, sorted(prices, key=lambda x: float(x)))
        (self.assertTrue(product['kids']) for product in products)

    def test_post_non_existing_product(self):
        """
        Creates a new product and returns it with a CREATED HTTP status code.
        """

        response = self.client.get(reverse('products:detail', kwargs={'pk': 9998}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        product = Product.objects.get(pk=51028)
        product.id = 9998
        serializer = ProductSerializer(product)
        response = self.client.post(reverse('products:index'), data=serializer.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(int(response.json()['id']), 9998)

    def test_post_existing_product(self):
        """
        Tries to create an already existing product and returns an info message
        with BAD_REQUEST HTTP status code.
        """

        response = self.client.get(reverse('products:detail', kwargs={'pk': 51028}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product = response.json()
        product = Product.objects.get(pk=int(51028))
        serializer = ProductSerializer(product)
        response = self.client.post(reverse('products:index'), data=serializer.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ProducstDetailTest(TestCase):
    """ProductsDetail view tests."""

    fixtures = ['test_products_all.json']

    def test_no_product(self):
        """
        Requesting a non existent product returns an empty message
        with NOT_FOUND HTTP status code.
        """
        response = self.client.get(reverse('products:detail', kwargs={'pk': 9999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_correct_product_request(self):
        """
        Requesting an existent product returns that single product
        with OK HTTP status code.
        """
        #   "model": "products.product",
        #   "pk": 44012,
        #   "fields": {
        #     "is_customizable": false,
        #   ...
        response = self.client.get(reverse('products:detail', kwargs={'pk': 44012}))
        self.assertEqual(int(response.json()['id']), 44012, )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_non_existing_product(self):
        """
        Deleting a non existent product returns an empty message
        with NOT_FOUND HTTP status code.
        """
        response = self.client.delete(reverse('products:detail', kwargs={'pk': 9999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_existing_product(self):
        """
        Deleting an existent product returns an empty message
        with NOT_CONTENT HTTP status code.
        """
        response = self.client.delete(reverse('products:detail', kwargs={'pk': 44241}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_non_existing_product(self):
        """
        PUTting a non existent product creates that product and
        returns that product with a CREATED HTTP status code.
        """
        response = self.client.get(reverse('products:detail', kwargs={'pk': 9995}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        product = Product.objects.get(pk=51028)
        product.id = 9995
        serializer = ProductSerializer(product)
        response = self.client.put(
            reverse('products:detail', kwargs={'pk': 9995}),
            content_type='application/json',
            data=json.dumps(serializer.data)
        )
        self.assertEqual(int(response.json()['id']), 9995)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_existing_product(self):
        """
        Updating an existent product returns the updated product
        with an OK status code.
        """
        response = self.client.get(reverse('products:detail', kwargs={'pk': 51028}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product = Product.objects.get(pk=51028)
        old_price = product.price
        product.price += 200
        serializer = ProductSerializer(product)
        response = self.client.put(
            reverse('products:detail', kwargs={'pk': 51028}),
            content_type='application/json', data=json.dumps(serializer.data)
        )
        self.assertNotEqual(float(response.json()['price']), float(old_price))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_existing_product_from_non_matching_id_url(self):
        """
        Updating an existent product from a non-matching URL
        returns a warning message with BAD_REQUEST HTTP status code.
        """
        response = self.client.get(reverse('products:detail', kwargs={'pk': 51028}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product = Product.objects.get(pk=51028)
        serializer = ProductSerializer(product)
        response = self.client.put(
            reverse('products:detail', kwargs={'pk': 9995}),
            content_type='application/json', data=json.dumps(serializer.data)
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
