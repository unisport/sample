import unittest
from ..models import UnisportAPI, UnisportAPIError

class UnisportAPITestCase(unittest.TestCase):

	def test_get_all_response_ok(self):
		unisport = UnisportAPI()
		result, status = unisport.get_all()

		self.assertEqual(status, 200)
