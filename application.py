import json

import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from helpers import DecimalJSONEncoder
from model.product import Product
from schema import ProductSchema, ProductSchemaDump

app = Flask(__name__)
app.json_encoder = DecimalJSONEncoder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/products.db'
app.config.update(DATABASE='data.json')
db = SQLAlchemy(app)


def _read_data(path):
    with open(path, 'r') as f:
        return json.load(f)


@app.route('/products')
def products():
    with app.app_context():
        products = Product.query.order_by(Product.price).all()
        return ProductSchemaDump().dump(products[:10], many=True)


@app.route('/products/kids')
def kids():
    with app.app_context():
        data = _read_data(app.config['DATABASE'])
        products = ProductSchema().load(data['products'], many=True).data
        products = filter(lambda item: item['kids'] == 1, products)
        products = sorted(products, cmp=lambda item1, item2: int(item1['price'] - item2['price']))
        return flask.jsonify(products)


if __name__ == '__main__':
    app.run()
