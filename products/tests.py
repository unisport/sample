from django.test import TestCase

class ProductsTestCase(TestCase):
	def test_call_root_redirect(self):
		response = self.client.get("/")
		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, "/products/")
		response = self.client.post("/")
		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, "/products/")
	
	def test_call_view_products_loads(self):
		response = self.client.get("/products/")
		self.assertEqual(response.status_code, 200)
		response = self.client.get("/products/kids/")
		self.assertEqual(response.status_code, 200)
		response = self.client.post("/products/")
		self.assertEqual(response.status_code, 200)
		response = self.client.post("/products/kids/")
		self.assertEqual(response.status_code, 200)
	
	def test_call_view_products_pages_loads(self):
		response = self.client.get("/products/", {"page": 1})
		self.assertEqual(response.status_code, 200)
		response = self.client.get("/products/kids/", {"page": 1})
		self.assertEqual(response.status_code, 200)

	def test_call_view_product_id_loads(self):
		response = self.client.get("/products/id/")
		self.assertEqual(response.status_code, 200)
		response = self.client.get("/products/id/1234/")
		self.assertEqual(response.status_code, 200)
		response = self.client.get("/products/id/157755/")
		self.assertEqual(response.status_code, 200)
		response = self.client.post("/products/id/")
		self.assertEqual(response.status_code, 200)
		response = self.client.post("/products/id/1234/")
		self.assertEqual(response.status_code, 200)
		response = self.client.post("/products/id/157755/")
		self.assertEqual(response.status_code, 200)