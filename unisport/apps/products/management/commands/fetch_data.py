import requests
from django.core.management.base import BaseCommand
from apps.products.models import Product
from django.utils.formats import sanitize_separators


class Command(BaseCommand):
    help = "Fetch data from specified url to app fixture."

    def add_arguments(self, parser):
        parser.add_argument('url', nargs=1, type=str)

    def handle(self, *args, **options):
        url = options['url'][0]
        self.stdout.write("Start loading data from '{0}' ...".format(url))
        source = requests.get(url)
        products = source.json()['products']

        for product in products:
            product['price'] = sanitize_separators(product['price'])
            product['price_old'] = sanitize_separators(product['price_old'])
            obj = Product(**product)
            obj.save()

        self.stdout.write("Data was succesfully fetched and saved to database.")
