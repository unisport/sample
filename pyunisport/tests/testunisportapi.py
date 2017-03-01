from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.core.urlresolvers import reverse
from rest_framework import status

class GetProductsTest(APITestCase):

	def test_get_products(self):
		url = reverse('get_products')
		response = self.client.get(url)

		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_kids_products(self):
		url = reverse('get_kids_products')
		response = self.client.get(url)

		self.assertEqual(response.status_code, status.HTTP_200_OK)

