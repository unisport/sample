import requests
import json

from django.core.management.base import BaseCommand
from django.conf import settings
from product_api.serializers import ProductSerializer


class Command(BaseCommand):
    help = 'Imports the products from Unisport Sample API.'

    def handle(self, *args, **options):

        api_response = requests.get(settings.API_URL)

        if api_response.status_code == 200:
            data = json.loads(api_response.text)['latest']

        # Duplicates will not be overwritten since we are using AutoField.
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
