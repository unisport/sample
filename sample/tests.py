from django.test import TestCase
import json
import urllib.request

# Reads the data from UniSport and makes it usable as JSON
urlData     = "http://www.unisport.dk/api/sample/"
webURL      = urllib.request.urlopen(urlData)
data 	    = webURL.read()
encoding    = webURL.info().get_content_charset('utf-8')
JSON_object = json.loads(data.decode(encoding))

# Create your tests here.
class ProductTestCase(TestCase):	
	# Ensures there is only success status code
	def test_call_view_get(self):
		response1 = self.client.get("/")
		self.assertEqual(response1.status_code, 200)
		response2 = self.client.get("/products")
		self.assertEqual(response2.status_code, 200)
		response3 = self.client.get("/products/kids/")
		self.assertEqual(response3.status_code, 200)
		response4 = self.client.get("/products/id/")
		self.assertEqual(response4.status_code, 200)
		response5 = self.client.get("/products/id/157755")
		self.assertEqual(response5.status_code, 200)
		# Tests what happens if the ID searched for does not exist
		response6 = self.client.get("/products/id/42/")
		self.assertEqual(response6.status_code, 200)

	# Ensures there is only success status code
	def test_call_view_post(self):
		response1 = self.client.post("/")
		self.assertEqual(response1.status_code, 200)
		response2 = self.client.post("/products")
		self.assertEqual(response2.status_code, 200)
		response3 = self.client.post("/products/kids/")
		self.assertEqual(response3.status_code, 200)
		response4 = self.client.post("/products/id/")
		self.assertEqual(response4.status_code, 200)
		response5 = self.client.post("/products/id/157755")
		self.assertEqual(response5.status_code, 200)
		# Tests what happens if the ID searched for does not exist
		response6 = self.client.post("/products/id/42/")
		self.assertEqual(response6.status_code, 200)

	# Ensures there is only success status code
	def test_call_view_pages(self):
		response1 = self.client.get("/products", {"page": 1})
		self.assertEqual(response1.status_code, 200)
		response2 = self.client.get("/products/kids/", {"page": 1})
		self.assertEqual(response2.status_code, 200)

	# Test if the sample data can be accessed
	def test_data_access(self):
		dataIsReadable = False				
		testdata = JSON_object
		try:
			if testdata['end-point'] == '/api/sample/':
				dataIsReadable = True
		except:
			dataIsReadable = False
		self.assertTrue(dataIsReadable)

	# Tests if the returned number of products is 10
	def test_10_products_returned(self):
		response = self.client.get('/products')
		self.assertEqual(len(response.context['products']), 10)

	# Tests that the product list is sorted correct (cheapest first)
	def test_cheapest_first(self):
		response = self.client.get('/products')
		prices = response.context['products'].object_list
		for i in range(10):
			if i == 0:
				# Cannot compare the first price to anything
				prev_price = prices[i]['price']
			else:
				# Need to change the data into floats, to compare accurately
				test = float(prev_price.replace(',','.')) <= float(prices[i]['price'].replace(',','.'))
				self.assertTrue(test)
				# Update the price, to be compared with the "next" previously
				prev_price = prices[i]['price']

	# Ensures that the producst shown are unique
	def test_no_duplicates(self):
		response = self.client.get('/products')
		products = response.context['products'].object_list
		for i in range(10):
			if i == 0:
				prev_product = products[i]['id']
			else:
				test = prev_product != products[i]['id']
				self.assertTrue(test)

	# Ensures that page=2 is different from the first page
	def test_different_pages(self):
		response1 = self.client.get('/products')
		response2 = self.client.get('/products?page=2')
		products1 = response1.context['products'].object_list
		products2 = response2.context['products'].object_list
		for i in range(10):
			test = products1[i]['id'] != products2[i]['id']
			self.assertTrue(test)

	# Tests that products/kids only have kids products and that they are sorted correctly (cheapest first)
	def test_only_kids_product(self):
		response = self.client.get('/products/kids')
		products = response.context['products'].object_list
		for i in range(len(products)):
			if i == 0:
				prev_price = products[i]['price']
				self.assertTrue(products[i]['kids'] == '1')
			else:
				test = float(prev_price.replace(',','.')) <= float(products[i]['price'].replace(',','.'))
				# Tests if the list is sorted correctly
				self.assertTrue(test)
				# Ensures that all products in this list is for kids
				self.assertTrue(products[i]['kids'] == '1')
				prev_price = products[i]['price']
	
	# Tests that the returned product from products/id/ is the correct
	# NOTE: Could test for all id's
	def test_id(self):
		response = self.client.get('/products/id/157755')
		product = response.context['product']
		self.assertTrue(product['id'] == '157755')

	# Ensures that the error message, when searching for an ID that does not exist, is displayed
	def test_id_invalid(self):
		response = self.client.get('/products/id/42')
		self.assertContains(response, '<p>There is no product with this ID</p>')