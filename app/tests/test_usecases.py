import StringIO
from unittest import TestCase
from app.data_source import StreamDataSource
from app.data_storage import StreamDataStorage
from app.models import Product
from app.usecases import get_product_by_id, get_kids_products_sorted_by_price, get_products_paginated, delete_product, \
    update_product, create_product


class TestGetProductById(TestCase):

    def test_basic(self):
        doc1 = Product(id="1")
        doc2 = Product(id="2")
        doc3 = Product(id="3")

        docs = [doc1, doc2, doc3]

        res = get_product_by_id(docs, "2")

        self.assertEqual(res, doc2)


class TestGetKidsProductsSortedByPrice(TestCase):

    def test_basic(self):

        doc1 = Product(id="1", kids="1", price="12,0")
        doc2 = Product(id="2", kids="1", price="111")
        doc3 = Product(id="3", kids="1", price="11,0")
        doc4 = Product(id="4", kids="0", price="12,0")

        docs = [doc1, doc2, doc3, doc4]

        res = get_kids_products_sorted_by_price(docs)

        self.assertEqual(res, [doc3, doc1, doc2])


class TestGetProductsPaginated(TestCase):

    def test_basic(self):
        doc1 = Product(id="432", kids="1", price="1,0")
        doc2 = Product(id="231", kids="0", price="2")
        doc3 = Product(id="313", kids="1", price="3,0")
        doc4 = Product(id="434", kids="0", price="5,0")
        doc5 = Product(id="42345", kids="0", price="62,0")
        doc6 = Product(id="1236", kids="1", price="1342,0")
        doc7 = Product(id="21327", kids="0", price="323412,0")
        doc8 = Product(id="3218", kids="0", price="13123322,0")
        doc9 = Product(id="9323", kids="1", price="11111111112,0")
        doc10 = Product(id="11230", kids="0", price="100000000000,0")

        docs = [doc6, doc1, doc7, doc2, doc5, doc10, doc3, doc4, doc8, doc9]

        res = get_products_paginated(docs, 1, 5)

        self.assertEqual(list(res), [doc6, doc7, doc8, doc9, doc10])


class TestDeleteProduct(TestCase):

    def test_basic(self):
        stream = StringIO.StringIO()

        stream_out = StreamDataStorage(stream)

        doc1 = Product(id="432", kids="1", price="1,0")
        doc2 = Product(id="231", kids="0", price="2")
        doc3 = Product(id="313", kids="1", price="3,0")

        docs = [doc1, doc2, doc3]

        stream_out.save_data(docs)

        stream.seek(0)

        stream_in = StreamDataSource(stream)

        delete_product(stream_in.get_data(), stream_out, doc2.id)

        stream.seek(0)
        new_docs = list(stream_in.get_data())

        self.assertEqual(len(new_docs), 2)
        self.assertFalse(new_docs[0].id == doc2.id)
        self.assertFalse(new_docs[1].id == doc2.id)


class TestUpdateProduct(TestCase):

    def test_basic(self):
        stream = StringIO.StringIO()

        stream_out = StreamDataStorage(stream)

        doc1 = Product(id="432", kids="1", price="1,0")
        doc2 = Product(id="231", kids="0", price="2")
        doc3 = Product(id="313", kids="1", price="3,0")

        docs = [doc1, doc2, doc3]

        stream_out.save_data(docs)

        stream.seek(0)
        stream_in = StreamDataSource(stream)

        doc2.price = "99,9"

        update_product(stream_in.get_data(), stream_out, doc2)

        stream.seek(0)
        new_docs = list(stream_in.get_data())

        self.assertEqual(len(new_docs), 3)
        self.assertTrue(
            (new_docs[0].price == "99,9") or
            (new_docs[1].price == "99,9") or
            (new_docs[2].price == "99,9")
        )


class TestCreateProduct(TestCase):

    def test_basic(self):
        stream = StringIO.StringIO()

        stream_out = StreamDataStorage(stream)

        doc1 = Product(id="432", kids="1", price="1,0")
        doc2 = Product(id="231", kids="0", price="2")
        doc3 = Product(id="313", kids="1", price="3,0")

        docs = [doc1, doc2, doc3]

        stream_out.save_data(docs)

        stream.seek(0)
        stream_in = StreamDataSource(stream)

        new_doc4 = Product(id="999", kids="1", price="39,0")

        create_product(stream_in.get_data(), stream_out, new_doc4)

        stream.seek(0)
        new_docs = list(stream_in.get_data())

        self.assertEqual(len(new_docs), 4)
        self.assertTrue(
            (new_docs[0].id == "999") or
            (new_docs[1].id == "999") or
            (new_docs[2].id == "999") or
            (new_docs[3].id == "999")
        )