import json
import pathlib
import unittest
from typing import Dict

from django.forms import model_to_dict
from django.test import TransactionTestCase
from hamcrest import assert_that, calling, equal_to, raises

from unisport.unisport_data.json import (
    Product,
    UnisportProducts,
    create_product_from_json,
    create_stock_from_json,
)
from unisport.unisport_data.models import Currency
from unisport.unisport_data.models import Product as ProductModel

TEST_FILE = pathlib.Path(__file__).parent.joinpath("data/response.json")


def load_test_data() -> Dict:
    with open(TEST_FILE, "r") as file:
        return json.load(file)


class TestDeserialiseUnisportData(unittest.TestCase):
    response_data: Dict = {}

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.response_data = load_test_data()

    def test_deserialize_unisport_products(self) -> None:
        expected_products_count = 13

        data = UnisportProducts(**TestDeserialiseUnisportData.response_data)

        assert_that(len(data.products), equal_to(expected_products_count))


class TestJSONToDBModel(TransactionTestCase):
    fixtures = ["currency"]
    response_data: Dict = {}

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.response_data = load_test_data()

    def setUp(self) -> None:
        self.product_json = TestJSONToDBModel.response_data["products"][0]
        self.product = Product(**self.product_json)

    def test_create_product_model_from_json_initialises_attributes(self) -> None:
        product_model = create_product_from_json(self.product)

        product_model_dict = model_to_dict(product_model)
        product_json_dict = self.product.dict(exclude={"stock", "prices"})
        product_json_dict.update(**self.product.prices.dict())

        assert_that(product_model_dict, equal_to(product_json_dict))

    def test_create_stock_model_from_json_initialises_attributes(self) -> None:
        stock = self.product.stock[0]
        stock_json_dict = stock.dict()
        stock_json_dict["id"] = stock_json_dict["pk"]
        stock_json_dict.pop("pk", None)

        stock_model_dict = model_to_dict(create_stock_from_json(stock))
        stock_model_dict.pop("product", None)

        assert_that(stock_model_dict, equal_to(stock_json_dict))

    def test_create_product_model_from_json_saves_product_to_db(self) -> None:
        product_model = create_product_from_json(self.product)

        db_product_model = ProductModel.objects.get(pk=product_model.id)

        assert_that(product_model, equal_to(db_product_model))

    def test_create_product_model_from_json_saves_stock_to_db(self) -> None:
        expected_stock_count = 1

        product_model = create_product_from_json(self.product)

        assert_that(
            len(product_model.stock_items.all()), equal_to(expected_stock_count)
        )

    def test_create_product_model_raises_error_for_unrecognised_currency(self) -> None:
        another_product_json = TestJSONToDBModel.response_data["products"][1]
        another_product = Product(**another_product_json)

        another_product.currency = "ABC"

        assert_that(
            calling(create_product_from_json).with_args(another_product),
            raises(Currency.DoesNotExist),
        )
