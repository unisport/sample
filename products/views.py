import json

from annoying.decorators import render_to
import requests

import models

API = 'http://www.unisport.dk/api/sample/'

@render_to('products/import.html')
def import_products(request):
    """
    Simple import. Enough for sample project.
    In the real life should be asynchronous(celery.task or something..) with validation, logging, etc.
    """

    for model in (models.Product, models.ProductSize):
        model.objects.all().delete()

    products = json.loads(requests.get(API).content).get('latest', [])

    for product in products:
        size_names = [size.strip() for size in product.pop('sizes', '').split(',')]

        product['product_id'] = product.pop('id')

        for field in ('price', 'price_old'):
            product[field] = product.get(field, '0').replace(',', '.')

        instance = models.Product.objects.create(**product)
        instance.sizes.add(*[models.ProductSize.objects.get_or_create(name=size_name)[0] for size_name in size_names])

    return {}
