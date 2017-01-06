import unittest

from selenium import webdriver
import requests

PRODUCT_FIXTURE = {
    "kids": "0",
    "name": "Gavekort",
    "sizes": "One Size",
    "kid_adult": "0",
    "free_porto": "0",
    "price": "0,00",
    "package": "0",
    "delivery": "1-2 dage",
    "url": "https://www.unisport.dk/gavekort/",
    "price_old": "0,00",
    "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/1_maxi_0.jpg",
    "women": "0",
}
API_TOKEN = 'token'


class ListProductsTest(unittest.TestCase):

    def setUp(self):
        """Open product listing page.
        """
        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000/products/')

    def tearDown(self):
        """Close browser.
        """
        self.browser.quit()

    def test_page_title(self):
        """Confirm that page title indicates that all products are listed.
        """
        self.assertEqual('Sport Shop - Products', self.browser.title)

    def test_thumbnail_count(self):
        """Confirm that pagination is working
        (don't show more than 10 products in one page).
        """
        thumbnails = self.browser.find_elements_by_class_name('thumbnail')
        self.assertTrue(len(thumbnails) <= 10)


class DetailProductTest(unittest.TestCase):

    def setUp(self):
        """Create new product using available endpoint
        (/products/create_product)
        Open detailed view page
        """
        # create product to test on
        new_product = PRODUCT_FIXTURE
        response = requests.post(
            'http://localhost:8000/products/create_product',
            json={'api_token': API_TOKEN, 'product': new_product}
        )
        self.product_id = response.json().get('product_id')
        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000/products/%s' % self.product_id)
        self.product_name = PRODUCT_FIXTURE.get('name')

    def tearDown(self):
        """Close browser
        Delete created product using available endpoint
        (/products/delete_product)
        """
        self.browser.quit()
        requests.post(
            'http://localhost:8000/products/delete_product',
            json={'api_token': API_TOKEN, 'product_id': self.product_id}
        )

    def test_page_title(self):
        """Confirm that product name is included in page title.
        """
        self.assertEqual('Sport Shop - %s' % self.product_name,
                         self.browser.title)

    def test_product_name(self):
        """Confirm that product name is shown as heading for product.
        """
        product_name = self.browser.find_element_by_class_name(
            'product-name').text
        self.assertEqual(product_name, self.product_name)
