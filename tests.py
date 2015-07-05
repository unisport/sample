import unittest
from django.test import TestCase
from django.core.management import call_command
from api.models import Product
import json

class ImportDataTest(TestCase):

    def test_import_command(self):
        call_command('import_data')
        products = Product.objects.all().count()
        self.assertEqual(products, 25)

class APITests(TestCase):
    fixtures = ['products.json']

    def setUp(self):
        self.list_url = '/products/'
        self.kids_url = '/products/kids/'
        self.detail_url = '/products/%d/'

    def test_list_products(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

        # test if only 10 elements were returned
        content = json.loads(response.content)
        self.assertEqual(len(content), 10)

        # test if the order is correct
        for i in range(len(content)-1):
            self.assertLessEqual(content[i]['price'], content[i+1]['price'])

    def test_pagination(self):
        # test 1st page
        response = self.client.get(self.list_url,{'page': 1})
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(len(content), 10)

        # test 2md page
        response = self.client.get(self.list_url,{'page': 2})
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(len(content), 10)

        # test 3rd page
        response = self.client.get(self.list_url,{'page': 3})
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(len(content), 5)

        # test 4th page
        response = self.client.get(self.list_url,{'page': 4})
        self.assertEqual(response.status_code, 404)

    def test_product_kids(self):
        response = self.client.get(self.kids_url)
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(len(content), 0)

    def test_product_detail(self):
        response = self.client.get(self.detail_url % 1)
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content['name'], 'Gavekort')
        self.assertEqual(content['price'], '0,00')
        self.assertEqual(content['kids'], '0')
        self.assertEqual(content['url'], 'http://www.unisport.dk/gavekort/')

        response = self.client.get(self.detail_url % 107)
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content['delivery'], '1-2 dage')
        self.assertEqual(content['price_old'], '1.099,00')
        self.assertEqual(content['kid_adult'], '1')
        self.assertEqual(content['img_url'], 'http://s3-eu-west-1.amazonaws.com/product-img/107_maxi_0.jpg')

        # product not found
        response = self.client.get(self.detail_url % 2)
        self.assertEqual(response.status_code, 404)

    def test_post(self):
        # valid data
        data = json.dumps({
            "kids": "1",
            "name": "Test",
            "sizes": "One Size",
            "kid_adult": "0",
            "free_porto": "0",
            "price": "0,00",
            "package": "0",
            "delivery": "1-2 dage",
            "url": "http://www.unisport.dk/gavekort/",
            "price_old": "1.200,0",
            "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/1_maxi_0.jpg",
            "women": "0",
        })
        response = self.client.post(self.list_url, data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        content = json.loads(response.content)
        self.assertEqual(content['status'], 'Created')
        self.assertEqual(content['product']['name'], 'Test')
        self.assertEqual(content['product']['price'], '0,00')
        self.assertEqual(content['product']['price_old'], '1.200,00')
        self.assertEqual(content['product']['kids'], '1')
        self.assertEqual(content['product']['url'], 'http://www.unisport.dk/gavekort/')
        test_product = Product.objects.filter(name='Test')
        self.assertEqual(test_product.count(), 1)
        self.assertEqual(test_product[0].name, 'Test')
        self.assertEqual(test_product[0].price, 0.00)
        self.assertEqual(test_product[0].price_old, 1200.00)
        self.assertEqual(test_product[0].kids, 1)
        self.assertEqual(test_product[0].url, 'http://www.unisport.dk/gavekort/')

        # invalid data format
        response = self.client.post(self.list_url, '{fsadf/..}', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        content = json.loads(response.content)
        self.assertEqual(content['status'], 'Invalid format')

        # data with validation errors
        data = json.dumps({
            "kids": "1",
            "name": "Test",
            "sizes": "One Size",
            "kid_adult": "0",
            "free_porto": "0",
            "price": "0,00",
            "package": "0",
            "delivery": "1-2 dage",
            "price_old": "0,00",
            "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/1_maxi_0.jpg",
            "women": "0",
        })
        response = self.client.post(self.list_url, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        content = json.loads(response.content)
        self.assertEqual(content['status'], 'Validation errors')
        self.assertEqual(content['errors']['url'][0], 'This field cannot be blank.')
        self.assertEqual(content['errors']['name'][0], 'Product with this Name already exists.')

        # data with invalid attribute
        data = json.dumps({
            "kids": "1",
            "name": "Test2",
            "description": "Test description",  # no such field on the Product model
            "sizes": "One Size",
            "kid_adult": "0",
            "free_porto": "0",
            "price": "0,00",
            "package": "0",
            "delivery": "1-2 dage",
            "url": "http://www.unisport.dk/gavekort/",
            "price_old": "0,00",
            "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/1_maxi_0.jpg",
            "women": "0",
        })

        response = self.client.post(self.list_url, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        content = json.loads(response.content)
        self.assertEqual(content['status'], 'Invalid attribute')

    def test_put(self):
        # valid data
        data = json.dumps({
            "name": "new name",
            "kids": "1",
            "price": "10,00",
            "url": "http://www.unisport.dk/newname/"
        })
        response = self.client.put(self.detail_url % 1, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content['name'], 'new name')
        self.assertEqual(content['kids'], '1')
        self.assertEqual(content['price'], '10,00')
        self.assertEqual(content['url'], 'http://www.unisport.dk/newname/')
        p = Product.objects.get(pk=content['id'])
        self.assertEqual(p.kids, 1)
        self.assertEqual(p.name, 'new name')
        self.assertEqual(p.kids, 1)
        self.assertEqual(p.price, 10.00)
        self.assertEqual(p.url, 'http://www.unisport.dk/newname/')

        # invalid data format
        response = self.client.put(self.detail_url % 1, '{fsadf/..}', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        content = json.loads(response.content)
        self.assertEqual(content['status'], 'Invalid format')

        # data with validation errors
        data = json.dumps({
            "kids": "yes",  # only True of False, 1 or 0
            "name": "Test",
            "sizes": "One Size",
            "kid_adult": "0",
            "free_porto": "0",
            "price": "price",  # must be a decimal
            "package": "0",
            "delivery": "1-2 dage",
            "price_old": "0,00",
            "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/1_maxi_0.jpg",
            "women": "0",
        })
        response = self.client.put(self.detail_url % 1, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        content = json.loads(response.content)
        self.assertEqual(content['status'], 'Validation errors')
        self.assertEqual(content['errors']['kids'][0], "'yes' value must be either True or False.")
        self.assertEqual(content['errors']['price'][0], "'price' value must be a decimal number.")

        # data with invalid attribute
        data = json.dumps({
            "kids": "1",
            "name": "Test2",
            "description": "Test description",  # no such field on the Product model
            "sizes": "One Size",
            "kid_adult": "0",
        })
        response = self.client.put(self.detail_url % 1, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        content = json.loads(response.content)
        self.assertEqual(content['status'], 'Invalid attribute')

    def test_delete(self):
        # create new product
        data = json.dumps({
            "kids": "1",
            "name": "F.C. K\u00f8benhavn",
            "sizes": "X-Large,XX-Large",
            "kid_adult": "1",
            "free_porto": "1",
            "price": "314.0",
            "package": "1",
            "delivery": "1-2 dage",
            "url": "http://www.unisport.dk/fodboldtroejer/fc-kbenhavn-trningstrje-condivo-14-blahvid/121796/",
            "price_old": "449.0",
            "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/121796_maxi_0.jpg",
            "women": "1",
            "id": 2,
        })
        response = self.client.post(self.list_url, data, content_type='application/json')
        self.assertEqual(Product.objects.filter(name='F.C. K\u00f8benhavn').count(), 1)

        # delete the product
        response = self.client.delete(self.detail_url % 2)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Product.objects.filter(name='F.C. K\u00f8benhavn').count(), 0)
