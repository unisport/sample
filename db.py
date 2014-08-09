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


def to_float(val):
    """ dk locale to python - breaks with thousand seperator"""
    return float(val.replace(',', '.'))

def to_bool(val):
    """ json string to py bool """
    if val == u'1' or val == u'True' or val == u'true':
        return True
    else:
        return False

# function map for casting to types
CONV = {'price':      to_float,
        'price_old':  to_float,
        'id':         int,
        'package':    to_bool,
        'free_porto': to_bool,
        'kids':       to_bool,
        'women':      to_bool,
        'kid_adult':  to_bool, }

DATA_PRE = json.loads(
    urllib2.urlopen('http://unisport.dk/api/sample').read())['latest']
# our in-memory "backend" database
DATA = {}
# cast keys to right type and save under product id
for o in DATA_PRE:
    for k in o.keys():
        f = CONV.get(k, None)
        if f:
            o[k] = f(o[k])
    DATA[o['id']] = o
