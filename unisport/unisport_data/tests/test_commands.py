from django.core.management import call_command
from django.test import TestCase, tag
from hamcrest import assert_that
from hamcrest.library.number.ordering_comparison import greater_than

from unisport.unisport_data import models


@tag("integration")
class CommandsTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        call_command("dataimport")

    def test_data_import_currency(self):
        assert_that(len(models.Currency.objects.all()), greater_than(0))

    def test_data_imported_products(self):
        assert_that(len(models.Product.objects.all()), greater_than(0))

    def test_data_imported_stock(self):
        assert_that(len(models.Stock.objects.all()), greater_than(0))
