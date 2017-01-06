from itertools import dropwhile
from itertools import tee
import unittest

import requests

BASE_URL = 'http://127.0.0.1:8000'


def pairwise(iterable):
    """Converts iterable in generator of tuples
    s -> (s0, s1), (s1, s2), (s2, s3), ..."""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def products_are_sorted(products):
    """Return True if products is sorted from smallest to biggest"""

    # We need compare prices
    prices = (float(product['price']) for product in products)

    # For that will find difference between each next item and prev ones
    deltas = (item2-item1 for (item1, item2) in pairwise(prices))

    # list with unsorted items. Must be empty
    not_sorted = list(dropwhile(lambda x: x >= 0, deltas))
    return not_sorted == []


class TestProducts(unittest.TestCase):

    def test_connection(self):
        """Main page returns 404 error"""
        r = requests.get(BASE_URL)
        self.assertEquals(r.status_code, 404)

    def test_json(self):
        """Response is data in JSON format"""
        r = requests.get(BASE_URL + '/products/')
        content_type = r.headers['content-type']
        self.assertIn(member='application/json', container=content_type)

    def test_contains_key_with_name_products(self):
        """JSON contains key with name 'products'"""
        r = requests.get(BASE_URL + '/products/')
        data = r.json()
        self.assertIn(member='products', container=data)

    def test_first_page_contains_10_products(self):
        """First page contains ten products"""
        r = requests.get(BASE_URL + '/products/')
        data = r.json()['products']
        self.assertEquals(len(data), 10)

    def test_second_page_contains_10_products(self):
        """First page contains ten products"""
        r = requests.get(BASE_URL + '/products/?page=2')
        data = r.json()['products']
        self.assertEquals(len(data), 10)

    def test_products_are_sorted(self):
        """Products sorted by price"""
        r = requests.get(BASE_URL + '/products/')
        products = r.json()['products']
        self.assertTrue(products_are_sorted(products))

    def test_kids(self):
        """Test that response contains only products for kids"""
        r = requests.get(BASE_URL + '/products/kids')
        products = r.json()['products']
        not_kids = (1 for product in products if product['kids'] != '1')
        self.assertEqual(sum(not_kids), 0)

    def test_kids_are_sorted(self):
        """Kids products sorted by price"""
        r = requests.get(BASE_URL + '/products/kids')
        products = r.json()['products']
        self.assertTrue(products_are_sorted(products))

    def test_id(self):
        """Product id equal to requested one"""
        r = requests.get(BASE_URL + '/products/')
        first_product_id = r.json()['products'][0]['id']
        r = requests.get(BASE_URL + '/products/%s' % first_product_id)
        product_id = r.json()['products'][0]['id']
        self.assertEqual(first_product_id, product_id)

    def test_id_only_one_item(self):
        """Test that response contains only one product"""
        r = requests.get(BASE_URL + '/products/')
        first_product_id = r.json()['products'][0]['id']
        r = requests.get(BASE_URL + '/products/%s' % first_product_id)
        products = r.json()['products']
        self.assertEqual(len(products), 1)

    def test_create_update_delete_product(self):
        data = {'action': 'add',
                'name': 'new added product',
                'price': '5.00',
                'package': '0',
                'free_porto': '0',
                'sizes': 'One Size',
                'women': '0',
                'url': 'https://www.unisport.dk/fodboldtroejer/newcastle-united-pin/314159/',
                'kid_adult': '0',
                'kids': '0',
                'delivery': '1-2 dage',
                'price_old': '29.00',
                'img_url': 'https://s3-eu-west-1.amazonaws.com/product-img/314159_maxi_0.jpg'
                }
        requests.post(BASE_URL + '/products/314159', data=data)
        r = requests.get(BASE_URL + '/products/314159')
        created_product = r.json()['products'][0]
        del(data['action'])
        del(created_product['id'])
        self.assertEqual(data, created_product)

        # test for product update
        data = {'action': 'update',
                'name': 'new added product2',
                'price': '8.00',
                'package': '1',
                'free_porto': '1',
                'sizes': "One Size",
                'women': '1',
                'url': "https://www.unisport.dk/fodboldtroejer/newcastle-united-pin/314159/",
                'kid_adult': '1',
                'kids': '1',
                'delivery': "1-2 dage",
                'price_old': "30.00",
                'img_url': "https://s3-eu-west-1.amazonaws.com/product-img/314159_maxi_0.jpg"
                }
        r = requests.post(BASE_URL + '/products/314159', data=data)
        self.assertEqual(r.status_code, 200)

        r = requests.get(BASE_URL + '/products/314159')
        created_product = r.json()['products'][0]
        del(data['action'])
        del(created_product['id'])
        self.assertEqual(data, created_product)

        data = {'action': 'delete'}
        r = requests.post(BASE_URL + '/products/314159', data=data)
        self.assertEqual(r.json()['status'], 'ok')
        r = requests.get(BASE_URL + '/products/314159')
        status = r.json()['status']
        reason = r.json()['reason']
        self.assertEqual(status, 'error')
        self.assertEqual(reason, 'ObjectDoesNotExist')
