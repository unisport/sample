from django.core.management.base import BaseCommand
from products.models import Product
from products.serializers import ProductSerializer
import json
from urllib.request import urlopen

DATA_SOURCE = 'https://www.unisport.dk/api/sample/'


class Command(BaseCommand):
    help = 'Populates database with sample information from https://www.unisport.dk/api/sample/'

    def handle(self, *args, **options):

        json_products = json.loads(urlopen(DATA_SOURCE).read())

        for product_json in json_products['products']:
            product_json['price'] = product_json['price'].replace('.', '').replace(',', '.')
            product_json['price_old'] = product_json['price_old'].replace('.', '').replace(',', '.')
            serializer = ProductSerializer(data=product_json)

            if serializer.is_valid():
                serializer.save()
            else:
                product = Product.objects.get(pk=int(product_json['id']))
                serializer = ProductSerializer(product, data=product_json)
                if serializer.is_valid():
                    serializer.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated database.'))
