# pylint: disable=missing-docstring, too-many-public-methods

import unittest
import db


class TestDBHelpers(unittest.TestCase):
    """ test import helper functions """

    def test_to_bool_true(self):
        for val in ('True', '1', 'true', ):
            self.assertTrue(db.to_bool(val), "'%s' is not True" % val)

    def test_to_bool_false(self):
        for val in ('Whatever', '0', 'False', 'false', ):
            self.assertFalse(db.to_bool(val))

    def test_to_float(self):
        tests = {
            '1.049,50': 1049.50,
            '345,90': 345.90,
            '7,0':    7.0,
            '42':     42.0, }
        for float_str, float_val in tests.items():
            self.assertEqual(db.to_float(float_str), float_val,
                             "'%s' does not eq %f" % (float_str, float_val))

class TestDB(unittest.TestCase):
    """ Test class for DB lookup """

    def setUp(self):
        db.DATA = {1: {'kids': False,
                       'name': 'item1',
                       'id': 1,
                       'price': 1.0},
                   5: {'kids': False,
                       'name': 'item5',
                       'id': 5,
                       'price': 5.0},
                   3: {'kids': False,
                       'name': 'item3',
                       'id': 3,
                       'price': 3.0},
                   2: {'kids': True,
                       'name': 'item2',
                       'id': 2,
                       'price': 2.0},
                   4: {'kids': True,
                       'name': 'item4',
                       'id': 4,
                       'price': 4.0},
                   7: {'kids': False,
                       'name': 'item7',
                       'id': 7,
                       'price': 7.0},
                   0: {'kids': True,
                       'name': 'item0',
                       'id': 0,
                       'price': 0.0, },
                   6: {'kids': True,
                       'name': 'item6',
                       'id': 6,
                       'price': 6.0}, }

    def test_get_three_cheapest_items(self):
        res = db.get_items_by_price(3)
        self.assertEqual(len(res), 3)
        self.assertEqual(res[0]['price'], 0.0)
        self.assertEqual(res[1]['price'], 1.0)
        self.assertEqual(res[2]['price'], 2.0)

    def test_get_two_cheapest_from_offset_four(self):
        res = db.get_items_by_price(2, 4)
        self.assertEqual(len(res), 2)
        self.assertEqual(res[0]['price'], 4.0)
        self.assertEqual(res[1]['price'], 5.0)

    def test_get_product(self):
        prod = db.get_product(4)
        self.assertEqual(prod['id'], 4)

if __name__ == "__main__":
    unittest.main()
