from django.test import TestCase
from ..models import Product

class ProductModelTests(TestCase):

	product_info = {
	    "is_customizable": "0",
	    "delivery": "None",
	    "kids": "0",
	    "name": "API product",
	    "sizes": "One Size",
	    "kid_adult": "0",
	    "free_porto": "0",
	    "image": "https://dxjm75mafwy8p.cloudfront.net/product/1/e1daa14a0ea9.jpg",
	    "package": "True",
	    "price": "200.00",
	    "url": "https://www.unisport.dk/gavekort/",
	    "price_old": "300.00",
	    "currency": "DKK",
	    "img_url": "https://dxjm75mafwy8p.cloudfront.net/product/1/e1daa14a0ea9.jpg",
	    "id": "3",
	    "women": "0",
	    "online": "0"
	}
	
	def test_create_product(self):
		"""
		Creating a product.
		"""

		product = Product.objects.create(**self.product_info)

		self.assertEqual(Product.objects.count(), 1)