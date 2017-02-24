# -*- coding: utf-8 -*-
import sys
import json
from models import Product
import codecs
import urllib2
import logging


def format_price(product):
    """
    Turns 0,00 into a real float
    """
    try:
        price = product['price'].replace(',', '.')
        return float(price)
    except KeyError:
        return float('0.00')


def kids_true(product):
    """
    Turns kids == 1 into a boolean instead
    """
    try:
        if product['kids'] == '1':
            return True
        else:
            return False
    except KeyError:
        return False


def format_id(product):
    """
    Turns the product id into an integer
    """
    return int(product['id'])


def format_name(product):
    """
    Ran into some weird encoding problem, tried to fix it by
    ensuring correct encoding. But really, ascii in a webservice?
    """
    return product['name'].encode('utf-8')


try:
    resp = urllib2.urlopen('http://www.unisport.dk/api/sample/')
    json_data = json.loads(resp.read())

    for product in json_data['products']:
        Product.create(name=format_name(product), price=format_price(product),
            for_kids=kids_true(product), product_id=format_id(product))

except urllib2.URLError, e:
    logging.warn(e)
