#!/usr/bin/env python

from flask import render_template, redirect, url_for, request

from sample import app
from sample.models import Item

@app.route('/products/<int:itemId>/')
def show_product_by_id(itemId):
  item = Item.by_id(itemId)
  if item: 
    return '<br>'.join([' : '.join([str(key), str(value)]) for key, value in
           item.__dict__.items() if not key.startswith("_")])
  else:
    return 'No item found'

@app.route('/products/<gender>/')
def show_product_by_gender(gender):
  if gender not in ['kids', 'kid_adult', 'women']:
    return "Not valid"

  items = Item.by_gender(gender)

  if items:
    return '<br><br>'.join(['<br>'.join([' : '.join([str(key), str(value)]) for key, value in
           item.__dict__.items() if not key.startswith("_")]) for item in items])
  else:
      return "No items found"
