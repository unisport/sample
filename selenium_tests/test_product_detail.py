import unittest
from selenium import webdriver


class ProductDetailTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_load_update_form(self):
		driver = self.driver
		driver.get('http://127.0.0.1:8000/products/')
		product1 = driver.find_elements_by_css_selector('h2>a')[0]
		product1.click()

		#>>>next page with current product detai and button 'update'
		
		title = driver.find_element_by_tag_name('h1')
		self.assertEqual(title.text, 'Product Detail')


	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()