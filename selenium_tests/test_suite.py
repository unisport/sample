import unittest

from test_product_list import ProductListDisplayingTest
from test_product_detail import ProductDetailTest




test_set1 = unittest.TestLoader().loadTestsFromTestCase(ProductListDisplayingTest)

test_set2 = unittest.TestLoader().loadTestsFromTestCase(ProductDetailTest)



test_suite = unittest.TestSuite([test_set1, test_set2])

unittest.TextTestRunner(verbosity=2).run(test_suite) 