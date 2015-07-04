import unittest
from django.test import TestCase
from django.core.management import call_command
from api.models import Product

class APITests(TestCase):

    def test_import_command(self):
        call_command('import_data')
        products = Product.objects.all().count()
        self.assertEqual(products, 25)
