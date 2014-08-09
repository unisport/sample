""" Load data and cast values to Python types

data will a dict with product id as key and product as value.
Each product is a dict with values cast to meaningful types

Notes:

First version of our main data structure was a list of products
as this it how it came from sample api.

I realized I had to casting to do when I saw prices was in DK locale.
I wrote a simple testcase under __main__ which I find useful as a minimal
testing "framework". Decided to cast a few others to bool (kids in particular)
and then product id to int.

When I had to get product by id I changed into a dict of products
with id as key (which I should have done up front)

"""

__author__ = "Jakob Goldbach"

import urllib2
import json

# our dict of products by product_id for fast lookup
DATA = {}

def to_float(val):
    """ dk locale to python """
    return float(val.replace('.', '').replace(',', '.'))

def to_bool(val):
    """ json string to py bool """
    if val == u'1' or val == u'True' or val == u'true':
        return True
    else:
        return False

def convert_types(obj):
    """ convert product fields to right types """
    conv = {'price':      to_float,
            'price_old':  to_float,
            'id':         int,
            'package':    to_bool,
            'free_porto': to_bool,
            'kids':       to_bool,
            'women':      to_bool,
            'kid_adult':  to_bool, }
    for k in obj.keys():
        f_cast = conv.get(k, None)
        if f_cast:
            obj[k] = f_cast(obj[k])
    return obj


def setup():
    """ initialize data from unisport """
    raw_list = json.loads(
        urllib2.urlopen('http://unisport.dk/api/sample').read())['latest']
    for product in raw_list:
        product = convert_types(product)
        # id now int
        DATA[product['id']] = product


def get_items_by_price(n_items=None, offset=0):
    """ get n_items elemenent at any offset """
    sort_prod = sorted(DATA.values(), key=lambda x: x['price'])
    if n_items:
        return sort_prod[offset:offset+n_items]
    else:
        return sort_prod

def get_product(pid):
    """ return product by product id """
    return DATA[pid]
