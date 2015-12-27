from selenium import webdriver
import unittest

class ListProductsTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000/products/')

    def tearDown(self):
        self.browser.quit()

    def test_page_title(self):
        self.assertEqual('Sport Shop - Products', self.browser.title)

    def test_thumbnail_count(self):
        thumbnails = self.browser.find_elements_by_class_name('thumbnail')
        self.assertEqual(len(thumbnails), 10)
