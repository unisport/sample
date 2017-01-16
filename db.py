""" Our database engine.

DATA is a dict of product with product_id as key.

Raw data from unisport.dk is imported and converted from DK locale
and bool/int/float strings to python ditto types.

Interface supports insert, delete, update and serching. See tests.py
for examples.

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

def get_product(pid):
    """ return product by product id """
    return DATA[pid]

def del_product(pid):
    """ delete product """
    del DATA[pid]

def get_all_products():
    """ return all products """
    return DATA.values()

def get_all_matching_products(**kwargs):
    """ search db for matching key-vals (AND match) """
    res = []
    for prod in get_all_products():
        for field, search_val in kwargs.items():
            if not field in prod:
                break
            if prod[field] != search_val:
                break
        else:
            res.append(prod)
    return res

def sort_by(lst, field):
    """ helper function to sort by field """
    return sorted(lst, key=lambda x: x[field])

def pick_items(lst, n_items=None, offset=0):
    """ helper function to pick n items from offset in array """
    if n_items:
        return lst[offset:offset+n_items]
    else:
        return lst[offset:]

def get_items_by_price(n_items=None, offset=0):
    """ get n_items elemenent at any offset """
    return pick_items(sort_by(get_all_products(), 'price'), n_items, offset)

def insert(json_data):
    """ insert dict by product id to database """
    DATA[json_data['id']] = json_data
    return DATA[json_data['id']]

def update(pid, json_data):
    """ update keys from submitted data to database """
    prod = get_product(pid)
    prod.update(json_data)
    DATA[pid] = prod
    return prod
