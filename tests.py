import unittest
import challenge
import json
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


def load_json(data):
	return json.loads(data)

class ChallengeTest(unittest.TestCase):
	
	
	def setUp(self):
		self.app = challenge.app.test_client()
	
	def test_products(self):
		products = load_json(self.app.get('/products/').data)['products']
		
		self.assertEqual(len(products), 10)

		prices = []
		
		for product in products:
			prices.append(locale.atof((product['price'])))
			
		for i in range(1, 10):
			self.assertGreaterEqual(prices[i], prices[i-1])
			