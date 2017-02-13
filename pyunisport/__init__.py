import locale
import requests
import json
from django.conf import settings

class UnisportAPI(object):

	def get_all(self):
		return self.request(None)	

	def request(
		self, path, args=None, post_args=None, method=None):

		if args is None:
			args = dict()
		if post_args is not None:
			method = "POST"

		if path is None:
			path = ''

		try:
			response = requests.request(
				method or "GET",
				settings.UNISPORT_ENDPOINT + path,
				params=args,
				data=post_args)
		except requests.HTTPError as e:
			response = json.loads(e.read())
			raise UnisportAPIError(response)

		headers = response.headers
		if 'json' in headers['content-type']:
			result = response.json()
		else:
			raise UnisportAPIError('Response not in json')


		if result and isinstance(result, dict) and result.get("error"):
			raise UnisportAPIError(result)
		return result

class UnisportAPIError(Exception):

	def __init__(self, result):
		self.result = result

		Exception.__init__(self, self.result)


class UniposortEndPoint(object):

	def __init__(self):

		self.unisprotapi = UnisportAPI()

	def get_all_products(self):

		return self.__get_all()

	def get_all_kids(self):

		data = self.unisprotapi.get_all()["products"]

		ordered_data = sorted(data, key=lambda k: locale.atof(k["price"]))

		result = [item for item in ordered_data if item["kids"] == "0"]

		return result



	def __get_all(self):
		return self.unisprotapi.get_all()
