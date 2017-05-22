import unittest
import json
import productservice
import mock
from unisport import app


class TestApi(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    # helper function for loading test fixture data
    def load_fixture(self, name):
        with open("fixtures/products.json") as data:
            return json.load(data)[name]

    # helper function for kids products
    def fixture_kids_products(self, name):
        products = self.load_fixture(name)
        return [product for product in products if product["kids"] == "1"]

    # helper function for loading products from api request
    # based on specified url
    def load_products(self, url):
        return json.loads(self.app.get(url).data)["products"]

    # helper function for mocking json response with no products
    def mock_no_products(self):
        return json.dumps({"products": []})

    # helper function for mocking json response with products
    def mock_products(self, name):
        return json.dumps({"products": self.load_fixture(name)})

    @mock.patch("productservice.urllib.urlopen")
    def test_get_products_no_data_should_return_no_products(self, up):
        up.return_value.read.return_value = self.mock_no_products()

        products = productservice.get_products()

        self.assertEqual(len(products), 0)

    @mock.patch("productservice.urllib.urlopen")
    def test_get_products_should_return_all_products(self, up):
        up.return_value.read.return_value = self.mock_products("products")

        products = productservice.get_products()
        fixture_products = self.load_fixture("products")

        self.assertEquals(products, fixture_products)

    @mock.patch("productservice.urllib.urlopen")
    def test_get_products_ordered_by_price_should_return_products(self, up):
        up.return_value.read.return_value = self.mock_products("products")

        products = productservice.get_products_ordered_by_price()
        fixture_products = self.load_fixture("ordered_products")

        self.assertEquals(products, fixture_products)

    @mock.patch("productservice.urllib.urlopen")
    def test_products_should_return_ten_products(self, up):
        up.return_value.read.return_value = self.mock_products("products")

        products = self.load_products("/products/")

        self.assertEqual(len(products), 10)

    @mock.patch("productservice.urllib.urlopen")
    def test_products_should_return_products_cheapest_first(self, up):
        up.return_value.read.return_value = self.mock_products("products")

        products = self.load_products("/products/")
        fixture_products = self.load_fixture("ordered_products")

        self.assertEquals(products, fixture_products[:10])

    @mock.patch("productservice.urllib.urlopen")
    def test_kids_products_should_return_ten_kids_products(self, up):
        up.return_value.read.return_value = self.mock_products("products")

        products = self.load_products("/products/kids/")

        self.assertEquals(len(products), 10)

    @mock.patch("productservice.urllib.urlopen")
    def test_kids_products_should_return_kids_products(self, up):
        up.return_value.read.return_value = self.mock_products("products")

        products = self.load_products("/products/kids/")
        fixture_products = self.fixture_kids_products("ordered_products")

        self.assertEquals(products, fixture_products)

if __name__ == '__main__':
    unittest.main()
