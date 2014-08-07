""" Load data and cast values to Python types

data will a dict with product id as key and product as value. Each product is a dict with values cast to meaningful types

Notes:

First version of our main data structure was a list of products as this it how it came from sample api.

I realized I had to casting to do when I saw prices was in DK locale. I wrote a simple testcase under __main__ which
I find useful as a minimal testing "framework". I decided to cast a few others to bool (kids in particular) and then product id to int

When I had to get product by id I changed into a dict of products with id as key (which I should have done up front)


"""

__author__ = "Jakob Goldbach"

import urllib2
import json


def to_float(s):
    s = s.replace(',', '.')
    return float(s)

def to_bool(s):
    if s == u'1' or s == u'True':
        return True
    else:
        return False

# function map for casting to types
conv = {'price':      to_float,
        'price_old':  to_float,
        'id':         int,
        'package':    to_bool,
        'free_porto': to_bool,
        'kids':       to_bool,
        'women':      to_bool,
        'kid_adult':  to_bool,
}

data_pre = json.loads(urllib2.urlopen('http://unisport.dk/api/sample').read())['latest']
# our in-memory "backend" database
data = {}
# cast keys to right type and save under product id
for o in data_pre:
    for k in o.keys():
        f = conv.get(k, None)
        if f:
            o[k] = f(o[k])
    data[o['id']]= o


if __name__ == "__main__":
    
    # minimal testing

    assert to_bool('2') == False
    assert to_bool('1') == True
    assert to_bool('0') == False
    assert to_float('346.45') == 346.45
    assert to_float('30') == 30.0

    product  = data.values()[0]
    assert isinstance(product['id'], int )
    assert isinstance(product['price'], float )
    assert isinstance(product['price'], float )
    
    assert product['price'] == 149.00
