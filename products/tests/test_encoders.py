import json

from django.test import TestCase

from products.encoders import ProductEncoder
from products.tests.utils import create_fake_product


class ProductEncoderTests(TestCase):

    def test_simple(self):
        # make sure it does not raise an error
        json.dumps({'product': create_fake_product()},
                   cls=ProductEncoder)

    def test_default_encoder_raises_an_error(self):
        with self.assertRaises(TypeError):
            json.dumps({'product': create_fake_product()})
