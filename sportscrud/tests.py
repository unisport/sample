import typing as t

import itertools
import json

from django.test import TestCase

from rest_framework.test import APIRequestFactory

from sportscrud.models import Product
from sportscrud import views


class TestDatabase(TestCase):
	fixtures = [
		'sample_data',
	]

	def test_database_initialization(self):
		""" Simple sanity check for the import of the sample data"""

		#Sample should contain 25 products
		self.assertEquals(len(Product.objects.all()), 25)

		#Boolean value parsed correctly
		self.assertEquals(Product.objects.get(pk=170941).online, True)


class TestApi(TestCase):
	fixtures = [
		'sample_data',
	]

	def _make_get_request(self, *, page: t.Optional[int] = None, kids: bool = False, pk: int = None) -> t.Dict:
		""" Just a simple private helper to avoid code duplication. Handling paginated objects could of course be
			done way better, probably by encapsulating it as an iterable, and lazily retrieving the data as needed,
			through the provided next link (or maybe with direct page indexing if indexing of the encapsulator is
			necessary). But this is just a helper in a unit test.
		"""

		# No endpoint for retrieving product by id through /kids
		self.assertFalse(kids and pk is not None)

		# Id retrieval is not paginated
		self.assertFalse(page is not None and pk is not None)

		factory = APIRequestFactory()

		request = factory.get(
			# f'sportscrud/products',
			# f'sportscrud/{"kids" if kids else "products"}',
			f'sportscrud/{"kids" if kids else "products"}/{"" if pk is None else pk}',
			data = {'page': page} if page is not None else None,
			format = 'json',
		)

		actions = {'get': 'list' if pk is None else 'retrieve'}

		view = (
			views.KidsViewSet.as_view(actions)
			if kids else
			views.ProductViewSet.as_view(actions)
		)

		response = view(request) if pk is None else view(request, pk=pk)
		# response = view(request)

		# Have to manually render the content
		response.render()

		# Check response is okay
		self.assertEquals(response.status_code, 200)

		return json.loads(response.content)

	def test_get_all(self):
		""" Make sure the list view of products is properly paginated, and returns the same amount of products
			as are present in the seed data.
		"""

		result_json = self._make_get_request()

		# The total count of objects is 25
		self.assertEquals(result_json['count'], 25)

		# Returns 10 objects, since it is paginated
		self.assertEquals(len(result_json['results']), 10)

	def _test_ordering(self, kids: bool):
		""" Helper determining whether collection endpoint returns products properly sorted by price ascending.
			The amount of divergent behaviour for kids maybe makes the slightly less code duplication not worth
			the hit for test transparency.

			@:param kids: True to test /kids endpoint only returning kids products
		"""

		products = []

		# Retrieve all products through api, presumable this could be done better by following the next link...
		for page in itertools.count(start=1, step=1):
			result = self._make_get_request(page=page, kids=kids)
			products.extend(result['results'])

			if result['next'] is None:
				break

		# Correct amount of products
		self.assertEquals(len(products), 3 if kids else 25)

		# If we are looking at the kids endpoint, make sure all the products are actually kids products.
		if kids:
			self.assertTrue(all(product['kids'] for product in products))

		# List of retrieved product prices
		prices = [product['price'] for product in products]

		# Product prices should be sorted ascending
		self.assertEquals(prices, sorted(prices))

		query_set = Product.objects.all().order_by('price')

		# Again, filter for kids if that is the endpoint we are looking at
		if kids:
			query_set = query_set.filter(kids=True)

		# Test against the sorted products retrieved from the orm for good measure
		orm_prices = [product.price for product in query_set]
		self.assertEquals(orm_prices, prices)

	def test_products_ordering(self):
		""" Test the ordering of /products endpoint"""

		self._test_ordering(kids=False)

	def test_kids_ordering(self):
		""" Test the ordering of the /kids endpoint"""

		self._test_ordering(kids=True)

	def test_get_specific(self):
		""" Test retrieval of products by id """

		# Test the name of the product corresponds to the name of the product retrieved through the api by id.
		# This notably does not check if any of the values match what they should be from the seed, only that the api
		# returns the right values corresponding to those in the database. I am uncertain how many values of the
		# sample data should be hardcoded in the tests. That verification should be left to other tests, this one
		# just checks the right data is served. (Also, i do not exhaustively check every field matches, here i just
		# assume the serialization is correct).
		for product in Product.objects.all():
			self.assertEquals(
				product.name,
				self._make_get_request(pk=product.pk)['name'],
			)