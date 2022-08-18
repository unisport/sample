from typing import List

from django.test import TestCase
from hamcrest import assert_that, equal_to

from unisport.unisport_data.models import Currency, Product, Stock


class TestProductProperties(TestCase):
    fixtures = ["currency"]

    product: Product
    stock_items: List[Stock] = []

    def setUp(self) -> None:
        self.product_under_test = TestProductProperties.product
        self.stock_items = TestProductProperties.stock_items

    @classmethod
    def setUpTestData(cls) -> None:
        cls.product = Product(
            id="12345",
            attributes={"test": "test"},
            labels={"labels": "labels"},
            name="name field",
            relative_url="v0/endpoint",
            image="https://www.example.com/images/image.jpg",
            delivery="deliver",
            online=True,
            is_customizable=False,
            is_exclusive=True,
            url="https://www.somethingelse.com/urls/url",
            max_price=1199,
            min_price=1199,
            currency=Currency.objects.get(pk="DKK"),
            discount_percentage=55,
            recommended_retail_price=1500,
        )
        cls.product.save()

        stock = Stock(
            id=123,
            name="stock_name",
            order_by=33,
            stock_info="",
            is_marketplace=False,
            name_short="stck",
            price=1199,
            product=cls.product,
        )

        another_stock = Stock(
            id=456,
            name="another_stock_name",
            order_by=34,
            stock_info="another_stock_info",
            is_marketplace=True,
            name_short="anthr_stck",
            price=2199,
            product=cls.product,
        )

        stock.save()
        another_stock.save()

        cls.stock_items.append(stock)
        cls.stock_items.append(another_stock)

    def test_product_stock_property_accessor_returns_expected_count(self) -> None:
        expected_total_stock_items = 2

        assert_that(
            self.product_under_test.stock.count(), equal_to(expected_total_stock_items)
        )

    def test_product_stock_property_access_returns_expected_data(self) -> None:
        actual_items = [stock for stock in self.product_under_test.stock]

        assert_that(actual_items, equal_to(self.stock_items))


class TestStr(TestCase):
    fixtures = ["currency"]

    def test_product_to_string(self) -> None:
        product = Product(
            id="12345",
            attributes={"test": "test"},
            labels={"labels": "labels"},
            name="name field",
            relative_url="v0/endpoint",
            image="https://www.example.com/images/image.jpg",
            delivery="deliver",
            online=True,
            is_customizable=False,
            is_exclusive=True,
            url="https://www.somethingelse.com/urls/url",
            max_price=1199,
            min_price=1199,
            currency=Currency.objects.get(pk="DKK"),
            discount_percentage=55,
            recommended_retail_price=1500,
        )

        product_str = f"{product.id} - {product.name}"

        assert_that(product_str, equal_to(str(product)))

    def test_stock_to_string(self) -> None:
        stock = Stock(
            id=123,
            name="stock_name",
            order_by=33,
            stock_info="",
            is_marketplace=False,
            name_short="stck",
            price=1199,
        )

        stock_str = f"{stock.id} - {stock.name_short}"

        assert_that(str(stock), equal_to(str(stock_str)))

    def test_currency_to_string(self) -> None:
        currency = Currency(
            id="DKK",
            description="Danish Kroner",
        )

        currency_str = f"{currency.id} - {currency.description}"

        assert_that(str(currency), equal_to(currency_str))


class TestGetAbsoluteUrl(TestCase):
    fixtures = ["currency"]

    def test_product_get_absolute_url(self) -> None:
        product = Product(
            id="12345",
            attributes={"test": "test"},
            labels={"labels": "labels"},
            name="name field",
            relative_url="v0/endpoint",
            image="https://www.example.com/images/image.jpg",
            delivery="deliver",
            online=True,
            is_customizable=False,
            is_exclusive=True,
            url="https://www.somethingelse.com/urls/url",
            max_price=1199,
            min_price=1199,
            currency=Currency.objects.get(pk="DKK"),
            discount_percentage=55,
            recommended_retail_price=1500,
        )

        expected_url = "/product/12345"

        url = product.get_absolute_url()

        assert_that(url, equal_to(expected_url))
