import json
from django.core.management.base import BaseCommand, CommandError
from api.models import Product
import argparse


class Command(BaseCommand):
    help = 'Imports a correctly formatted JSON file'

    def add_arguments(self, parser):
        parser.add_argument('PATH', nargs='+', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        for file in options['PATH']:
            with file as f:
                data = json.loads(f.read())
                products = data['products']
                for product in products:
                    p = Product(
                        is_customizable=bool(int(product['is_customizable'])),
                        delivery=product['delivery'],
                        kids=bool(int(product['kids'])),
                        name=product['name'],
                        package=bool(int(product['package'])),
                        kid_adult=bool(int(product['kid_adult'])),
                        free_porto=bool(int(product['free_porto'])),
                        thumbnail=product['image'],
                        sizes=product['sizes'],
                        price=int(
                            product['price']
                            .replace(',','').replace('.','')),
                        discount_type=product['discount_type'],
                        online=bool(int(product['online'])),
                        price_old=int(
                            product['price']
                            .replace(',','').replace('.','')),
                        currency=product['currency'],
                        img_url=product['img_url'],
                        id=int(product['id'])
                    )
                    p.save()
