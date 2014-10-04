from app.models import Product
import types
from unittest import TestCase
from app.data_filters import PaginationFilter, SortingFilter, KeyValueFilter, CompositeFilter


class TestPaginationFilter(TestCase):

    def test_basic(self):
        res = PaginationFilter(0, 5).apply(
            xrange(10)
        )

        self.assertTrue(type(res), types.GeneratorType)
        self.assertEqual(list(res), [0, 1, 2, 3, 4])

        res = PaginationFilter(1, 3).apply(
            xrange(10)
        )
        self.assertEqual(list(res), [3, 4, 5])

    def test_over_bounds(self):
        res = PaginationFilter(10, 3).apply(
            xrange(10)
        )
        self.assertEqual(list(res), [])


class TestSortingFilter(TestCase):

    def test_asc(self):

        doc1 = Product(value=1)
        doc2 = Product(value=2)
        doc4 = Product(value=4)
        doc5 = Product(value=5)

        res = SortingFilter(SortingFilter.ASC, 'value').apply(
            [doc5, doc2, doc4, doc1]
        )

        self.assertTrue(type(res), types.GeneratorType)
        self.assertEqual(list(res), [doc1, doc2, doc4, doc5])

    def test_desc(self):

        doc1 = Product(value=1)
        doc2 = Product(value=2)
        doc4 = Product(value=4)
        doc5 = Product(value=5)

        res = SortingFilter(SortingFilter.DESC, 'value').apply(
            [doc5, doc2, doc4, doc1]
        )

        self.assertTrue(type(res), types.GeneratorType)
        self.assertEqual(list(res), [doc5, doc4, doc2, doc1])


class TestKeyValueFilter(TestCase):

    def test_basic(self):

        doc1 = Product(title="Nike Boots", kids="0")
        doc2 = Product(title="Adidas Boots", kids="0")
        doc3 = Product(title="Loli t-shirt", kids="1")
        doc4 = Product(title="Mickey Mouse Cap", kids="1")
        doc5 = Product(title="Puma T-Shirt", kids="0")

        res = KeyValueFilter(key='kids', value="1").apply(item for item in [doc1, doc2, doc3, doc4, doc5])

        self.assertTrue(type(res), types.GeneratorType)
        self.assertEqual(list(res), [doc3, doc4])

    def test_inverse(self):
        doc1 = Product(title="Nike Boots", kids="0")
        doc2 = Product(title="Adidas Boots", kids="0")
        doc3 = Product(title="Loli t-shirt", kids="1")
        doc4 = Product(title="Mickey Mouse Cap", kids="1")
        doc5 = Product(title="Puma T-Shirt", kids="0")

        res = KeyValueFilter(key='kids', value="1", inverse=True).apply(item for item in [doc1, doc2, doc3, doc4, doc5])

        self.assertTrue(type(res), types.GeneratorType)
        self.assertEqual(list(res), [doc1, doc2, doc5])


class TestCompositeFilter(TestCase):

    def test_basic(self):

        doc1 = Product(title="Nike Boots", kids="0", id="4")
        doc2 = Product(title="Adidas Boots", kids="0", id="2")
        doc3 = Product(title="Loli t-shirt", kids="1", id="6")
        doc4 = Product(title="Mickey Mouse Cap", kids="1", id="5")
        doc5 = Product(title="Puma T-Shirt", kids="0", id="3")
        doc6 = Product(title="Puma T-Shirt", kids="0", id="1")

        composite_filter = CompositeFilter(
            KeyValueFilter(key='kids', value="0"),
            SortingFilter(SortingFilter.ASC, "id")
        )

        res = composite_filter.apply([doc1, doc2, doc3, doc4, doc5, doc6])
        self.assertEqual(res, [doc6, doc2, doc5, doc1])
