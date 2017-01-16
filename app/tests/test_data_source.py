import StringIO
from unittest import TestCase
from app.data_source import StreamDataSource
from app.models import Product


class TestStreamDataSource(TestCase):

    def test_basic(self):
        ds = StreamDataSource(StringIO.StringIO(
            '''{ "latest": [
{
  "kids": "1",
  "name": "adidas - Spilletr\u00f8je Striped Estro 13 Sort/R\u00f8d B\u00f8rn",
  "sizes": "128 cm/8 years,140 cm/10 years,152 cm/12 years",
  "kid_adult": "0",
  "free_porto": "False",
  "price": "99,00",
  "package": "0",
  "delivery": "1-2 dage",
  "url": "http://www.unisport.dk/fodboldudstyr/adidas-spilletroje-striped-estro-13-sortrod-born/99903/",
  "price_old": "199,00",
  "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/99903_da_mellem.jpg",
  "id": "99903",
  "women": "0"
} ] }
            '''
        ))

        data = list(ds.get_data())

        self.assertEqual(len(data), 1)
        self.assertIsInstance(data[0], Product)
        self.assertEqual(data[0].id, "99903")