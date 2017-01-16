import StringIO
from unittest import TestCase
from app.data_storage import StreamDataStorage
from app.models import Product


class TestStreamDataSource(TestCase):

    def test_basic(self):
        stream = StringIO.StringIO()
        ds = StreamDataStorage(stream)

        doc = Product(id="1", price="99,99")

        ds.save_data([doc, doc])

        self.assertEqual(
            stream.getvalue(),
            '{"latest": [{"price": "99,99", "id": "1"}, {"price": "99,99", "id": "1"}]}'
        )