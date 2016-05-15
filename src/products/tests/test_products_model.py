from django.test import TestCase

from ..models import Product


class ProductModelTests(TestCase):
    

    def test_unicode(self):
    	"Test Product model field string output"
        product = Product(
        	name='Test name',
			currency='DKK',
			delivery='1-2 days',
			price='1',
			price_old='10')

        self.assertEqual(unicode(product), 'Test name')
        # or 
        self.assertEqual(product.__unicode__(), 'Test name')

