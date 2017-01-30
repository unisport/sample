import json
import urllib.request
from decimal import Decimal

from django.core.management.base import BaseCommand

from products.models import Product


class Command(BaseCommand):
    help = 'Populates the products table with data from the specified source'

    def add_arguments(self, parser):
        parser.add_argument(
            '--source',
            default='http://www.unisport.dk/api/sample/',
        )
        parser.add_argument(
            '--overwrite-existing',
            action='store_true',
            help='Determines whether the existing products with the same ids '
                 'will be overwritten or left untouched.',
        )

    def handle(self, *args, **options):
        url = options['source']
        overwrite_existing = options['overwrite_existing']

        with urllib.request.urlopen(url) as response:
            status_code = response.getcode()
            assert status_code == 200, ('Unexpected HTTP status code: {}'
                                        .format(status_code))

            data = json.load(response)
            self.stdout.write('Extracted data from {}'.format(url))

        for product_data in data['products']:
            self._add_product(product_data, overwrite_existing)

    def _add_product(self, product_data, overwrite_existing):
        product_id = int(product_data['id'])
        try:
            instance = Product.objects.get(id=product_id)
            product_exists = True
        except Product.DoesNotExist:
            instance = Product(id=product_id)
            product_exists = False

        if product_exists:
            if overwrite_existing:
                msg = ('Overwriting product #{} with the data from the '
                       'source.'.format(product_id))
                self.stdout.write(self.style.WARNING(msg))
            else:
                msg = ('Skipped the product #{}, because it already exists'
                       ' in the database. '.format(product_id))
                self.stdout.write(msg)
                return

        self._copy_data_to_instance(product_data, instance)
        instance.save()

    def _copy_data_to_instance(self, data, instance):
        instance.is_customizable = int(data['is_customizable'])
        instance.delivery = data['delivery']
        instance.kids = int(data['kids'])
        instance.name = data['name']
        instance.package = int(data['package'])
        instance.kid_adult = int(data['kid_adult'])
        instance.free_porto = int(data['free_porto'])
        instance.image = data['image']
        instance.sizes = data['sizes']
        instance.price = self._parse_price(data['price'])
        instance.url = data['url']
        instance.online = int(data['online'])
        instance.price_old = self._parse_price(data['price_old'])
        instance.currency = data['currency']
        instance.img_url = data['img_url']
        instance.women = int(data['women'])

    @staticmethod
    def _parse_price(price_str):
        head, tail = price_str.rsplit(',', 1)
        head = head.replace('.', '')
        value = Decimal('{}.{}'.format(head, tail))
        return value
