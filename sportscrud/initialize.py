import typing as t

import requests as r

from sportscrud.models import Product


class DatabaseInitializer(object):

	_TARGET_URL = 'https://www.unisport.dk/api/sample/'

	@classmethod
	def _string_to_float(cls, s: str) -> float:
		return float(s.replace('.', '').replace(',', '.'))

	@classmethod
	def _populate(cls, products: t.List[t.Dict[str, t.Any]]) -> None:
		Product.objects.bulk_create(
			Product(
				is_customizable = product['is_customizable'],
				delivery = product['delivery'],
				kids = product['kids'],
				name = product['name'],
				relative_url = product['relative_url'],
				discount_percentage = product['discount_percentage'],
				kid_adult = product['kid_adult'],
				free_porto = product['free_porto'],
				image = product['image'],
				sizes = product['sizes'],
				package = product['package'],
				price = cls._string_to_float(product['price']),
				discount_type = product['discount_type'],
				product_labels = product['product_labels'],
				url = product['url'],
				online = product['online'],
				price_old = cls._string_to_float(product['price_old']),
				currency = product['currency'],
				img_url = product['img_url'],
				id = product['id'],
				women = product['women'],
			)
			for product in
			products
		)

	@classmethod
	def initialize(cls):
		result = r.get(cls._TARGET_URL)

		if not result.ok or not result.json():
			raise RuntimeError(f'Remote sample not available: {result.status_code}')

		Product.objects.all().delete()

		cls._populate(result.json()['products'])