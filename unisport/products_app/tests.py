from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json
from products_app.models import Products




class AccountTests(APITestCase):
    fixtures = ['dump.json']

    def test_product_link(self):
        """
        test /products/ link.
        """
        response = self.client.get('/products/')
        results = response.data['results']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(results), 10)

        unsorded_price = get_unsorted_prise_list(results)
        self.assertEqual(unsorded_price, sorted(unsorded_price))

    def test_product_page_link(self):
        """
        test /products/?page=2 link.
        """
        response = self.client.get('/products/?page=2')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data['results']
        self.assertEqual(len(results), 10)

        unsorded_price = get_unsorted_prise_list(results)
        self.assertEqual(unsorded_price, sorted(unsorded_price))

    def test_product_kids_link(self):
        """
        test /products/kids/ link.
        """
        response = self.client.get('/products/kids/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        no_kids = [x['kids'] for x in response.data if x['kids']==0 ]
        self.assertEqual(len(no_kids), 0)

    def test_product_id_link(self):
        """
        test /products/id/ link.
        """
        product = Products.objects.all()[1]
        response = self.client.get('/products/'+str(product.id)+'/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], product.id)

    def test_create_product_link(self):
        """
        create product with post method
        """
        new_prod = {
            'name': 'saaaz1z',
            'sizes': '2',
            'delivery': "2",
            'price': "0.00",
            'price_old': "0.00",
            'url': "",
            'img_url': "",
            'kids': 0,
            'women': 0,
            'kid_adult': 0,
            'free_porto': 0,
            'package': 0
        }

        response = self.client.post('/products/', new_prod, format=None)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_product_link(self):
        """
        update product with patch method
        """
        product = Products.objects.all()[1]
        response = self.client.patch('/products/'+str(product.id)+'/', {'sizes':'1234'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product = Products.objects.all()[1]
        self.assertEqual(product.sizes, '1234')

    def test_delete_product_link(self):
        """
        delete product with patch method
        """
        product = Products.objects.all()[1]
        response = self.client.delete('/products/'+str(product.id)+'/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

def get_unsorted_prise_list(price_list):
    return [ float(k['price']) for k in price_list]