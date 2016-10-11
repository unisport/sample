import requests

from flask import Flask, jsonify, abort
app = Flask(__name__)

PRODUCTS = sorted(requests.get('http://www.unisport.dk/api/sample/').json()
                  ['products'], key=lambda k: float(k['price'].replace(',', '.')))

@app.route('/products')
def products():
    return jsonify(PRODUCTS[:10])

@app.route('/products/page/<int:number>')
def products_page(number):
    return jsonify(PRODUCTS[number*10-10:number*10])

@app.route('/products/kids')
def products_kids():
    return jsonify([product for product in PRODUCTS if product['kids'] == '1'])

@app.route('/products/<id>')
def product(id):
    for product in PRODUCTS:
        if product['id'] == id:
            return jsonify(product)
    abort(404)
