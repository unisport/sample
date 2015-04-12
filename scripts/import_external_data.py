#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import urllib2
import json
p = os.path


# -- Init django context -- --

sys.path.append(p.abspath(p.join(p.dirname(__file__), '..')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'
import django
django.setup()

# -- -- -- --

from unisample.api.product.models import Product

sample_url = 'http://www.unisport.dk/api/sample/'
sample_data = urllib2.urlopen(sample_url).read()

print 'Fetched data'

try:
    sample_data = json.loads(sample_data)
except Exception as e:
    print 'Was unable to parse sample data', e.message
    exit()

sample_data = sample_data and sample_data.get('latest')

if not sample_data:
    print "Error: Expected to have top-level 'latest' element in json data"
    exit()

# -- -- -- --

# note: specific to current sample data
def to_decimal(val):
    return val.replace('.', '').replace(',', '.')

print 'Start importing data'

item_added = 0
for data in sample_data:
    try:
        Product.objects.create(
            name = data['name'],

            price     = to_decimal(data['price']),
            price_old = to_decimal(data['price_old']),

            kids      = data['kids'],
            kid_adult = data['kid_adult'],
            women     = data['women'],

            delivery   = data['delivery'],
            free_porto = data['free_porto'],
            package    = data['package'],

            sizes      = data['sizes'],

            url = data['url'],
            img_url = data['img_url'],
        )

        item_added += 1

    except Exception as e:
        print 'Warning! Error while adding product: ', e

print 'Done! Added {} items'.format(item_added)

