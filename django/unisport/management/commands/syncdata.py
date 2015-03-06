import json
import urllib2
from django.core.management.base import BaseCommand

from unisport import models


class Command(BaseCommand):
    help = 'Sync database with the data from the API sample.'

    def handle(self, *args, **options):
        data_url = 'http://www.unisport.dk/api/sample/'
        products_json = json.loads(urllib2.urlopen(data_url).read())

        products = {}
        for product_json in products_json['latest']:
            fake_id = int(product_json['id'])
            ## Data types clean-up and conversions.
            # ID 131971 appears twice, I don't know if this is a mistake or not,
            # using a dict guarantees uniqueness.
            products[fake_id] = {
                'fake_id': fake_id,
                'kids': bool(int(product_json['kids'])),
                'kid_adult': bool(int(product_json['kid_adult'])),
                'women': bool(int(product_json['women'])),
                'package': bool(int(product_json['package'])),
                'free_porto': product_json['free_porto'] == 'True',
                'url': product_json['url'],
                'img_url': product_json['img_url'],
                'price': float(product_json['price'].replace(',', '.')),
                'price_old': float(
                    product_json['price'].replace('.', '').replace(',', '.')
                ),
                'name': product_json['name'],
                'delivery': product_json['delivery'],
                'sizes': product_json['sizes'],
            }

        models.Product.objects.bulk_create([
            models.Product(**product_data) for product_data in products.values()
        ])
