from unittest import TestCase
from app.models import Document
from app.usecases import get_product_by_id, get_kids_products_sorted_by_price, get_products_paginated


class TestGetProductById(TestCase):

    def test_basic(self):
        doc1 = Document(id="1")
        doc2 = Document(id="2")
        doc3 = Document(id="3")

        docs = [doc1, doc2, doc3]

        res = get_product_by_id(docs, "2")

        self.assertEqual(res, doc2)


class TestGetKidsProductsSortedByPrice(TestCase):

    def test_basic(self):

        doc1 = Document(id="1", kids="1", price="12,0")
        doc2 = Document(id="2", kids="1", price="111")
        doc3 = Document(id="3", kids="1", price="11,0")
        doc4 = Document(id="4", kids="0", price="12,0")

        docs = [doc1, doc2, doc3, doc4]

        res = get_kids_products_sorted_by_price(docs)

        self.assertEqual(res, [doc3, doc1, doc2])


class TestGetProductsPaginated(TestCase):

    def test_basic(self):
        doc1 = Document(id="432", kids="1", price="1,0")
        doc2 = Document(id="231", kids="0", price="2")
        doc3 = Document(id="313", kids="1", price="3,0")
        doc4 = Document(id="434", kids="0", price="5,0")
        doc5 = Document(id="42345", kids="0", price="62,0")
        doc6 = Document(id="1236", kids="1", price="1342,0")
        doc7 = Document(id="21327", kids="0", price="323412,0")
        doc8 = Document(id="3218", kids="0", price="13123322,0")
        doc9 = Document(id="9323", kids="1", price="11111111112,0")
        doc10 = Document(id="11230", kids="0", price="100000000000,0")

        docs = [doc6, doc1, doc7, doc2, doc5, doc10, doc3, doc4, doc8, doc9]

        res = get_products_paginated(docs, 1, 5)

        self.assertEqual(list(res), [doc6, doc7, doc8, doc9, doc10])
