import unittest
from sportr import sportr


class TestUtilities(unittest.TestCase):
    def test_manipulate_data_empty_list(self):
        items, ids = sportr.manipulate_data([])
        self.assertEqual(items, [])
        self.assertEqual(ids, {})

    def test_manipulate_data_simple(self):
        data = [{'sizes': '1, 2, 3, 4', 'id': '1234'}, {'sizes': ',1,2,3,4,', 'id': '1111'}]
        items, ids = sportr.manipulate_data(data)
        self.assertEqual(items, [
            {'sizes': ['1', '2', '3', '4'], 'id': '1234'},
            {'sizes': ['1', '2', '3', '4'], 'id': '1111'}
        ])
        self.assertEqual(ids, {'1234': 0, '1111': 1})
        self.assertEqual(len(items), len(ids))
        self.assertEqual(len(data), len(ids))
