import requests

from django.core.management.base import BaseCommand

from api.models import Product
from api.serializers import ProductSerializer

# Predefined API query that get 25 products
PRODUCTS_URL = 'https://www.unisport.dk/api/products/batch/?list=176719,201504,193289,188311,158873,201502,158419,203123,201442,195978,203122,130083,184297,183734,160479,170474,168438,171411,170705,195991,183293,170486,181055,202060,193271'


class Command(BaseCommand):
    help = 'Clears the databse and fetches products from an external API to save them in the database'

    def handle(self, *args, **options):
        resp = requests.get(PRODUCTS_URL)

        if not resp.ok:
            self.stdout.write(self.style.ERROR(f'Error occured when connecting to products API: {resp.status_code} {resp.reason}'))
            return

        # Clear database table
        Product.objects.all().delete()

        products = resp.json()
        for product in products['products']:

            # Your API must have changed since the requirements were posted
            # I assume this makes up for the missing "kids" key
            product['kids'] = product['attribute_english']['age'][0] == 'Kids'

            # Create Product entry in the database
            serializer = ProductSerializer(data=product)
            if serializer.is_valid():
                serializer.save()
            else:
                self.stdout.write(self.style.ERROR(f'Unable to serialize product {product.get("id", "UNKNOWN ID")}'))

        self.stdout.write(self.style.SUCCESS('Successfully fetched products'))
