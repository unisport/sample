"""
    sportr
    ~~~~~~

    A webservice presenting the data found at http://www.unisport.dk/api/sample/.
    Exposes the following endpoints:
    /products/
    /products/kids
    /products/?page=n
    /products/id/

    :author: Carl Bordum Hansen
"""

from flask import Flask, render_template, request
import requests


app = Flask(__name__)


def fetch_data(url):
    """Request json data from *url* and return the list where key == 'products'."""
    return requests.get(url).json()['products']


def manipulate_data(data):
    """Return a list of data and a mapping with id/index pairs."""
    items = []
    id_lookup = {}
    for index, item in enumerate(data):
        # convert sizes from str to list for easier rendering in jinja (and no empty strings)
        item['sizes'] = [s.strip() for s in item['sizes'].split(',') if s]
        items.append(item)
        id_lookup[item['id']] = index
    return items, id_lookup


url = 'http://www.unisport.dk/api/sample/'
# use two data structures
# sacrifice space for O(1) response at /products/id/
items, id_lookup = manipulate_data(fetch_data(url))


@app.route('/products/')
def products():
    """If page arg *n* is passed (e.g /products/?page=2); return the items from
    n*10 - 10 to n*10. Else return the 10 first items ordered cheapest first."""
    n = request.args.get('page', default=1, type=int)
    return render_template('index.html', items=items[n*10-10:n*10], title='products')


@app.route('/products/kids/')
def kid_products():
    """Return all items where kids=1 ordered cheapest first."""
    kid_items = []
    for item in items:
        if item['kids'] == '1':
            kid_items.append(item)
    return render_template('index.html', items=kid_items, title='kid products')


@app.route('/products/<ID>/')
def product_by_id(ID):
    """Return the product with id=ID."""
    return render_template('index.html', items=[items[id_lookup[ID]]], title=ID)
