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

    def test_pick_four_items(self):
        lst = range(20)
        res = db.pick_items(lst, 4)
        self.assertEqual(len(res), 4)

    def test_pick_three_items_from_offset_eight(self):
        lst = range(20) # 0...19
        # n=3
        # offset=0: 0,1,2
        # offset=1: 1,2,3
        # offset=8: 8,9,10
        res = db.pick_items(lst, 3, 8)
        self.assertEqual(res[0], 8)
        self.assertEqual(res[1], 9)
        self.assertEqual(res[2], 10)
        
    def test_to_many(self):
        lst = range(20)
        res = db.pick_items(lst, 5, 18)
        self.assertEqual(len(res), 2)


class TestDB(unittest.TestCase):
    """ Test class for DB lookup """

    def setUp(self):
        db.DATA = {0: {'kids': True,
                       'name': 'item0',
                       'id': 0,
                       'price': 10.0, },
                   1: {'kids': False,
                       'name': 'item1',
                       'id': 1,
                       'price': 9.0},
                   2: {'kids': True,
                       'name': 'item2',
                       'id': 2,
                       'price': 8.0},
                   3: {'kids': False,
                       'name': 'item3',
                       'id': 3,
                       'price': 7.0},
                   4: {'kids': True,
                       'name': 'item4',
                       'id': 4,
                       'price': 5.0},
                   5: {'kids': False,
                       'name': 'item5',
                       'id': 5,
                       'price': 4.0},
                   6: {'kids': True,
                       'name': 'item6',
                       'id': 6,
                       'price': 4.0}, }
                       
    def test_get_three_cheapest_items(self):
        res = db.get_items_by_price(3)
        self.assertEqual(len(res), 3)
        self.assertEqual(res[0]['price'], 4.0)
        self.assertEqual(res[1]['price'], 4.0)
        self.assertEqual(res[2]['price'], 5.0)

    def test_get_two_cheapest_from_offset_four(self):
        res = db.get_items_by_price(2, 4)
        self.assertEqual(len(res), 2)
        self.assertEqual(res[0]['price'], 8.0)
        self.assertEqual(res[1]['price'], 9.0)

    def test_get_product(self):
        prod = db.get_product(4)
        self.assertEqual(prod['id'], 4)

    def test_get_products(self):
        res = db.get_all_products()
        self.assertEqual(len(res), 7)

    def test_get_price_is_four(self):
        res = db.get_all_matching_products(price=4.0)
        self.assertEqual(len(res), 2)
        for prod in res:
            self.assertEqual(prod['price'], 4.0)

    def test_get_kids_and_price_is_four(self):
        res = db.get_all_matching_products(kids=True,price=4.0)
        self.assertEqual(len(res), 1)
        for prod in res:
            self.assertTrue(prod['kids'])
            self.assertEqual(prod['price'], 4.0)
        
    def test_get_kids(self):
        for prod in db.get_all_matching_products(kids=True):
            self.assertTrue(prod['kids'])

    
if __name__ == "__main__":
    unittest.main()
