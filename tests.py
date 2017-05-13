import unittest
import challenge
import json
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

ITEMS_PER_PAGE = 10
ITEM_ID = '1'

def load_json(data):
	return json.loads(data)


class ChallengeTest(unittest.TestCase):
	
	
	def setUp(self):
		self.app = challenge.app.test_client()
	
	def test_products(self):
		products = load_json(self.app.get('/products/').data)['products']
		
		self.assertEqual(len(products), ITEMS_PER_PAGE)
		
		prices = [locale.atof(product['price']) for product in products]
		
		for i in range(1, len(prices)):
			self.assertGreaterEqual(prices[i], prices[i-1])

	def test_products_kids(self):
		products = load_json(self.app.get('/products/kids/').data)['products']
		
		for product in products:
			self.assertEqual(product['kids'], '1')

	def test_products_page(self):
		page = load_json(self.app.get('/products/?page=2').data)
		self.assertEqual(page['page'], 2)

	def test_products_invalid_page(self):
		page = load_json(self.app.get('/products/?page=a').data)
		self.assertEqual(page['page'], 0)
	
	def test_products_id(self):
		product = load_json(self.app.get('/products/' + ITEM_ID + '/').data)['product']
		self.assertEqual(product['id'], ITEM_ID)
		