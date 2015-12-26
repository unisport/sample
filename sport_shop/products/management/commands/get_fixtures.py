import json

from django.core.management.base import BaseCommand, CommandError
import requests

from products.models import Product

FIXTURE_URL = 'https://www.unisport.dk/api/sample/'


def download_json(url=FIXTURE_URL):
    response = requests.get(url)
    return response.json()


def save_product(product_data):
    product = Product(**product_data)
    try:
        product.save()
    except Exception, err:
        print product_data
        raise err
    return product


class Command(BaseCommand):
    help = 'Downloads product fixtures.'

    def handle(self, *args, **options):
        data = download_json()
        products = data.get('products')
        for product_data in products:
            save_product(product_data)
