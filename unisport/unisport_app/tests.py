from django.test import Client
import unittest

class Tests(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    def test_products_page(self):
        response = self.client.get('/products/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('count'), 12)
        self.assertEqual(len(response.json().get('results')), 10)

        pricelist = []

        for product in response.json().get('results'):
            pricelist.append(product.get('prices').get('recommended_retail_price'))
        for i in range(1,10):
            assert pricelist[i] >= pricelist[i-1]
    
    def test_second_page(self):
        response = self.client.get('/products/?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json().get('results')), 2)
        
        pricelist = []

        for product in response.json().get('results'):
            pricelist.append(product.get('prices').get('recommended_retail_price'))
        for i in range(1,2):
            assert pricelist[i] >= pricelist[i-1]

    def test_product_by_id(self):
        id = 172011
        response = self.client.get(f"/products/{id}/")
        self.assertEqual(response.json().get('id'),id)


