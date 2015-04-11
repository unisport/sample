#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests

url = 'http://127.0.0.1:8000/api/products/add/'

data = {
     "name": "Product Name",

     "price": 209.0,
     "price_old": 349.0,

     "kids": 1,
     "women": 0,
     "kid_adult": 0,

     "delivery": "1-2 dage",
     "free_porto": True,
     "package": 0,
     "sizes": "EU 27\u00bd/US 10\u00bdC",

     "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/121973_da_mellem.jpg",
     "url": "http://www.unisport.dk/fodboldstoevler/nike-fc247-elastico-pro-iii-tf-orangesortneon-brn/121973/",
}


# -- Add product --

r = requests.post(url, data)
print r.content

res = json.loads(r.content)

# -- Edit product --

url = 'http://127.0.0.1:8000/api/products/{}/edit/'.format(res['product_pk'])

data["name"] = "New Product Name"

r = requests.post(url, data)
print r.content

# -- Get product --

url = 'http://127.0.0.1:8000/api/products/{}/'.format(res['product_pk'])

r = requests.get(url)
print r.content

# -- Delete product --

url = 'http://127.0.0.1:8000/api/products/{}/delete/'.format(res['product_pk'])

r = requests.post(url)
print r.content
