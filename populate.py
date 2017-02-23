import sys
import json
from models import Product
import codecs


def format_price(product):
    try:
        price = product['price'].replace(',', '.')
        return float(price)
    except KeyError:
        return float('0.00')


def kids_true(product):
    try:
        if product['kids'] == '1':
            return True
        else:
            return False
    except KeyError:
        return False


def format_id(product):
    return int(product['id'])


def format_name(product):
    return unicode(product['name'].strip(codecs.BOM_UTF8), 'utf-8')

with open('sample.json') as json_data:
    products = json.load(json_data)

    for product in products['products']:
        Product.create(name=product['name'], price=format_price(product),
            for_kids=kids_true(product), product_id=format_id(product))

