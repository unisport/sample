import requests
from django.core.management.base import BaseCommand

from products.constants import URL
from products.models import Product


class Command(BaseCommand):
    help = 'Import products from Unisport'

    def handle(self, *args, **options):
        response = requests.get(URL)
        products = response.json()['products']
        for product in products:
            Product.objects.create(
                id=int(product['id']),
                name=product['name'],
                price=int(product['price'])/100,
                image=product['product_main_image'],
                meta=product
            )
        self.stdout.write(self.style.SUCCESS('Successfully imported products'))
