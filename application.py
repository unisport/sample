import json
import flask
from flask import Flask
from schema import ProductSchema
from helpers import DecimalJSONEncoder


app = Flask(__name__)
app.json_encoder = DecimalJSONEncoder
PATH = 'data.json'


def _read_data(path):
    with open(path, 'r') as f:
        return json.load(f)


@app.route('/products')
def products():
    with app.app_context():
        data = _read_data(PATH)
        products = ProductSchema().load(data['products'], many=True).data
        products = sorted(products, cmp=lambda item1, item2: int(item1['price'] - item2['price']))
        return flask.jsonify(products[:10])


@app.route('/products/kids')
def kids():
    with app.app_context():
        data = _read_data(PATH)
        products = ProductSchema().load(data['products'], many=True).data
        products = filter(lambda item: item['kids'] == 1, products)
        products = sorted(products, cmp=lambda item1, item2: int(item1['price'] - item2['price']))
        return flask.jsonify(products)


if __name__ == '__main__':
    app.run()
