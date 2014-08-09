import unittest

from db import to_bool, to_float, DATA

class TestDBHelpers(unittest.TestCase):

    def test_to_bool_true(self):
        for v in ('True', '1', 'true', ):
            self.assertTrue(to_bool(v), "'%s' is not True" % v)

    def test_to_bool_false(self):
        for v in ('Whatever', '0', 'False', 'false', ):
            self.assertFalse(to_bool(v))

    def test_to_float(self):
        tests = {'345,90': 345.90,
                 '7,0':    7.0,
                 '42':     42.0, }
        for k, v in tests.items():
            self.assertEqual(to_float(k), v, "'%s' does not eq %f" % (k, v))

    def test_types(self):
        product = DATA.values()[0]
        self.assertIsInstance(product['id'], int)
        self.assertIsInstance(product['price'], float)

if __name__ == "__main__":
    unittest.main()

