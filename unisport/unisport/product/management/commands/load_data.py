#coding: utf-8
import json
from django.core.management import BaseCommand
import requests
from unisport.product import models
from unisport.product.forms import ProductForm
from unisport.product.service import get_price_from_unicode


class Command(BaseCommand):
    help = u'This command will load data from https://www.unisport.dk/api/sample/ and write to database'

    def handle(self, *args, **options):
        url = 'http://www.unisport.dk/api/sample/'
        response = requests.get(url)
        if response.status_code != 200:
            return self.stdout.write('Not expected response from https://www.unisport.dk/api/sample/')
        try:
            products = json.loads(response.text)['products']
        except (ValueError, KeyError):
            return self.stdout.write('Invalid products format')

        models.Product.objects.all().delete()

        for product in products:
            product['price'] = get_price_from_unicode(product['price'])
            product['price_old'] = get_price_from_unicode(product['price_old'])
            form = ProductForm(product)
            if not form.is_valid():
                self.stdout.write('wrong data in product with id - %s' % product['id'])
                continue
            form.save()
        self.stdout.write('Products successfully loaded ')

