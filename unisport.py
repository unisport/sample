import productservice
from flask import Flask, jsonify
from locale import setlocale, LC_ALL


app = Flask(__name__)
setlocale(LC_ALL, "")


@app.route('/products/')
def products():
    products = productservice.get_products_ordered_by_price()

    return jsonify({"products": products[:10]})


@app.route('/products/kids/')
def kids_products():
    products = productservice.get_kids_products()

    return jsonify({"products": products})
