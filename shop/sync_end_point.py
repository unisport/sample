#!/usr/bin/env python
# -*- encoding: UTF-8 -*-
"""
Propose: Sync data from end-point to DataBase
Author: 'yac'
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")
import django
django.setup()
import urllib2
import json

from products.models import Product

print 'Start sync DataBase with end-point...'
req = urllib2.Request('https://www.unisport.dk/api/sample/')

try:
    file_object = urllib2.urlopen(req)
except urllib2.URLError:
    raise

data = file_object.read()
products = json.loads(data)

print 'Saving products to DataBase'
for product in products['products']:
    product['id_ext'] = product.pop('id')

    Product(**product).save()

print 'DataBase sync finished.'
