import unittest
from selenium import webdriver


class ProductListDisplayingTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_product_list_display(self):
		"Test displaying Product list page and the first product displaying"

		#Of course if we have 'and' in our test description beter to divide it on 2 tests
		#But they are simply and I joined them together
		driver = self.driver
		driver.get('http://127.0.0.1:8000/products/')
		self.assertIn("Unisport", driver.title)
		elem = driver.find_element_by_tag_name('h1')
		self.assertEqual(elem.text, 'Products list')
		try:
			product1 = driver.find_elements_by_css_selector('h2>a')[0]
		except:
			raise Exception ('Products list page has no displayed products!!!')
		self.assertIn ('/products/', product1.get_attribute('href'), 
			'Link to product_detail does not exist')

	def test_product_list_paginate(self):
		"Test pagination"

		driver = self.driver
		driver.get('http://127.0.0.1:8000/products/')
		products_list_page = driver.find_elements_by_css_selector('h2>a')
		self.assertEqual(len(products_list_page), 10, 
			'Pagination does not work properly or we have less products than pagination range')



	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()