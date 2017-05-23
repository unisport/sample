import unittest
import json
import productservice
import mock
import seeder
from unisport import app, ITEMS_PER_PAGE, db
from flask_testing import TestCase
from models import Product


class TestApi(TestCase):

    # required method for test setup
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dev_sample.db'
        app.config['TESTING'] = True

        return app

    @mock.patch("seeder.urllib.urlopen")
    def setUp(self, urlopen):
        db.create_all()
        urlopen.return_value.read.return_value = self.mock_products("products")
        seeder.run(db)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # helper function for loading test fixture data
    def load_fixture(self, name):
        with open("fixtures/products.json") as data:
            return json.load(data)[name]

    # helper function for loading fixture kids products
    def fixture_kids_products(self, name):
        products = self.load_fixture(name)
        return [product for product in products if product["kids"] == "1"]

    # helper function for loading products from api request
    # based on specified url
    def load_products(self, url):
        client = self.app.test_client()
        return json.loads(client.get(url).data)["products"]

    # helper function for loading product ids from api request
    def load_product_ids(self, url):
        products = self.load_products(url)
        return [product["id"] for product in products]

    # helper function for mocking json response with no products
    def mock_no_products(self):
        return json.dumps({"products": []})

    # helper function for mocking json response with products
    def mock_products(self, name):
        return json.dumps({"products": self.load_fixture(name)})

    # helper function for loading fixture product ids
    def fixture_product_ids(self, name):
        products = self.load_fixture(name)

        return [int(product["id"]) for product in products]

    # helper function for loading fixture product prices
    def fixture_product_prices(self, name):
        products = self.load_fixture(name)

        return [seeder.format_price(product["price"]) for product in products]

    def test_get_products_no_data_should_return_no_products(self):
        db.drop_all()
        db.create_all()

        products = productservice.get_products()

        self.assertEqual(len(products), 0)

    def test_get_products_should_return_all_products(self):
        products = productservice.get_products()
        fixture_products = self.load_fixture("products")

        self.assertEquals(len(products), len(fixture_products))

    def test_get_products_ordered_by_price_should_return_products(self):
        products = productservice.get_products_ordered_by_price()
        products_ids = [product["id"] for product in products]

        fixture_ids = self.fixture_product_ids("ordered_products")

        self.assertEquals(products_ids, fixture_ids)

    def test_get_product_unknown_id_should_return_product(self):
        product = productservice.get_product(2)

        self.assertEqual(product, None)

    def test_get_product_valid_id_should_return_product(self):
        product = productservice.get_product(153638)

        self.assertEqual(product["id"], 153638)

    def test_products_should_return_ten_products(self):
        products = self.load_products("/products/")

        self.assertEqual(len(products), 10)

    def test_products_should_return_products_cheapest_first(self):
        products = self.load_products("/products/")
        prices = [product["price"] for product in products]

        fixture_prices = self.fixture_product_prices("ordered_products")

        self.assertEquals(prices, fixture_prices[:ITEMS_PER_PAGE])

    def test_kids_products_should_return_ten_kids_products(self):
        products = self.load_products("/products/kids/")

        self.assertEquals(len(products), 10)

    def test_kids_products_should_return_kids_products(self):
        products_ids = self.load_product_ids("/products/kids/")

        fixture_products = self.fixture_kids_products("ordered_products")
        fixture_ids = [int(product["id"]) for product in fixture_products]

        self.assertEquals(products_ids, fixture_ids)

    def test_products_page_empty_should_return_first_ten_products(self):
        products_ids = self.load_product_ids("/products/?page=")

        fixture_ids = self.fixture_product_ids("ordered_products")

        self.assertEquals(products_ids, fixture_ids[:ITEMS_PER_PAGE])

    def test_products_page_0_should_return_first_ten_products(self):
        products_ids = self.load_product_ids("/products/?page=0")

        fixture_ids = self.fixture_product_ids("ordered_products")

        self.assertEquals(products_ids, fixture_ids[:ITEMS_PER_PAGE])

    def test_products_page_negative_should_return_first_ten_products(self):
        products_ids = self.load_product_ids("/products/?page=-1")

        fixture_ids = self.fixture_product_ids("ordered_products")

        self.assertEquals(products_ids, fixture_ids[:ITEMS_PER_PAGE])

    def test_products_page_1_should_return_first_ten_products(self):
        products_ids = self.load_product_ids("/products/?page=1")

        fixture_ids = self.fixture_product_ids("ordered_products")

        self.assertEquals(products_ids, fixture_ids[:ITEMS_PER_PAGE])

    def test_products_page_2_should_return_next_ten_products(self):
        products_ids = self.load_product_ids("/products/?page=2")

        fixture_ids = self.fixture_product_ids("ordered_products")

        self.assertEquals(products_ids, fixture_ids[10:20])

    def test_products_page_out_of_bounds_should_return_no_products(self):
        products = self.load_products("/products/?page=4")

        self.assertEquals(len(products), 0)

    def test_products_page_invalid_should_return_first_ten_products(self):
        products_ids = self.load_product_ids("/products/?page=a")

        fixture_ids = self.fixture_product_ids("ordered_products")

        self.assertEquals(products_ids, fixture_ids[:ITEMS_PER_PAGE])

    def test_product_unknown_id_should_return_404(self):
        response = self.app.test_client().get("/products/2/")

        self.assertEqual(response.status_code, 404)

    def test_product_invalid_id_should_return_404(self):
        response = self.app.test_client().get("/products/i/")

        self.assertEqual(response.status_code, 404)

    def test_product_by_valid_id_should_return_product(self):
        data = self.app.test_client().get("/products/153638/").data
        product = json.loads(data)["product"]

        self.assertEqual(product["id"], 153638)

    def test_create_product_valid_should_return_201(self):
        new_product = dict(self.load_fixture("new_product"))

        response = self.app.test_client().post(
            "/products/create/",
            data=new_product
        )

        self.assertEqual(response.status_code, 201)

    def test_create_product_after_creation_products_count_should_be_26(self):
        new_product = dict(self.load_fixture("new_product"))

        response = self.app.test_client().post(
            "/products/create/",
            data=new_product
        )

        self.assertEqual(db.session.query(Product).count(), 26)

    def test_update_product_valid_should_return_201(self):
        product = self.load_fixture("products")[0]
        product["delivery"] = "2-3 dage"

        response = self.app.test_client().put(
            "/products/153339/edit/",
            data=dict(product)
        )

        updated_product = json.loads(response.data)["product"]

        self.assertEqual(response.status_code, 201)

    def test_update_product_should_return_updated_product(self):
        product = self.load_fixture("products")[0]
        product["delivery"] = "2-3 dage"

        response = self.app.test_client().put(
            "/products/153339/edit/",
            data=dict(product)
        )

        updated_product = json.loads(response.data)["product"]

        self.assertEqual(updated_product["delivery"], "2-3 dage")

    def test_update_product_should_return_the_same_product(self):
        product = self.load_fixture("products")[0]
        product["delivery"] = "2-3 dage"

        response = self.app.test_client().put(
            "/products/153339/edit/",
            data=dict(product)
        )

        updated_product = json.loads(response.data)["product"]

        self.assertEqual(updated_product["id"], int(product["id"]))

    def test_delete_product_after_deletion_product_count_should_be_24(self):
        response = self.app.test_client().delete("/products/153339/delete/")

        self.assertEqual(db.session.query(Product).count(), 24)

    def test_delete_product_with_id_153339_should_return_200(self):
        response = self.app.test_client().delete("/products/153339/delete/")

        self.assertEqual(response.status_code, 200)

    def test_delete_product_with_id_153339_should_not_exist_when_deleted(self):
        response = self.app.test_client().delete("/products/153339/delete/")

        result = db.session.query(Product).get(153339)

        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
