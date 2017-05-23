import productservice
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from locale import setlocale, LC_ALL
from math import ceil


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample.db'
db = SQLAlchemy(app)
setlocale(LC_ALL, "")
ITEMS_PER_PAGE = 10


@app.route('/products/')
def products():
    page = request.args.get("page", 1, int)
    products = productservice.get_products_ordered_by_price()

    if(page is None or page <= 0):
        page = 1
    elif(page > ceil(len(products) / float(ITEMS_PER_PAGE))):
        return jsonify({"products": []})

    offset = (page - 1) * ITEMS_PER_PAGE

    return jsonify({"products": products[offset:page * ITEMS_PER_PAGE]})


@app.route('/products/kids/')
def kids_products():
    products = productservice.get_kids_products()

    return jsonify({"products": products})


@app.route('/products/<int:id>/')
def product(id):
    product = productservice.get_product(id)

    if product is None:
        return jsonify({'error': 'Product not found'}), 404

    return jsonify({"product": product})
