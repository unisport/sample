import requests
import json

from django.core.management.base import BaseCommand, CommandError
from product_api.models import Product
from product_api.serializers import ProductSerializer


class Command(BaseCommand):
    help = 'Imports the products from Unisport Sample API.'

    def handle(self, *args, **options):
        api_url ='http://www.unisport.dk/api/sample/'
        api_response = requests.get(api_url)

        if api_response.status_code == 200:
            data = json.loads(api_response.text)['latest']

        # All duplicates will be overwritten.
        for item in data:

            # Initial price and price_old are in German locale.
            # Prepare those values for storing in Decimal type.
            item['price'] = item['price'].replace('.', '').replace(',', '.')
            item['price_old'] = item['price_old'].replace('.', '').replace(',', '.')

            serializer = ProductSerializer(data=item)

            if serializer.is_valid():
                serializer.save()
            else:
                self.stdout.write("Item has invalid fields: {}".format(item))
                self.stdout.write("Errors: {}".format(serializer.errors))

        self.stdout.write("Successfully imported all products.")
