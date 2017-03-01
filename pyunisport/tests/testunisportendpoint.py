import unittest
from ..models import UniposortEndPoint

class UniposortEndPointTestCase(unittest.TestCase):

	def test_get_all_products_type(self):

		endpoint = UniposortEndPoint()
		data = endpoint.get_all_products()
		self.assertEqual(list, type(data))

	def test_get_all_kids_products_type(self):

		endpoint = UniposortEndPoint()
		data = endpoint.get_all_products()
		self.assertEqual(list, type(data))
