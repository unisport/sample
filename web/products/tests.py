import json

from rest_framework.test import APITestCase
from django.urls import reverse
from products.serializers import ProductSerializer

"""
I tryed to implement testing as well, but I have to admit that my knowledge at this point is to little to do it with success
I have left the code as a reference till later.
"""
class ProductsApiTest(APITestCase):
    def setUp(self):
        self.products_url = "/products/"
  
    def test_get_ten_items_from_api(self):
        response = self.client.get(self.products_url)
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.content)
        self.assertEqual(10, len(response_data))
