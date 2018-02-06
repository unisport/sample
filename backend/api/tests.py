from django.test import TestCase, Client
from api.models import Product

# Create your tests here.
c = Client()


class ProductTests(TestCase):
    def test_converting_to_string(self):
        product = Product(
            name="Test product",
            is_customizable=False,
            delivery="Soon",
            kids=False,
            package=False,
            kid_adult=False,
            free_porto=True,
            thumbnail=None,
            sizes="One size",
            price=10000,
            discount_type="None",
            online="True",
            price_old=10000,
            currency="DKK",
            img_url=None,
            id=1337
        )
        self.assertIs(str(product), "Test product")
