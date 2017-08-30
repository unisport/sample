import requests, json
from flask import Flask, request, jsonify, abort
app = Flask(__name__)

def get_product_list():
    json_response = requests.get("https://www.unisport.dk/api/sample/")
    products = json_response.json()['products']
    return products

def get_sorted_product_list():
    products = get_product_list()    
    #We sort the array by price, name immediately since we'll always want it in that order.
    products.sort(key=lambda p: (float(p['price'].replace(',', '.')), p['name']))
    return products

@app.route('/')
@app.route('/products/', methods=["GET"])
def get_products_for_page(page=1):
    products = get_sorted_product_list()

    page_number = request.args.get('page', 1, type=int)
    if page_number <= 0:
        abort(404)

    index_start = (page_number - 1) * 10
    #Slicing lists with [x:y] goes from x to y-1, so we add 10 to the end instead of 9
    index_end = index_start + 10

    return jsonify({"products" : products[index_start:index_end]})

@app.route('/products/kids/', methods=["GET"])
def get_kids_products():
    products = list((single_product for single_product in get_sorted_product_list() if single_product['kids'] == '1'))

    return jsonify({"products" : products})

@app.route('/products/<product_id>/', methods=["GET"])
def get_product_by_id(product_id):
    products = get_product_list()

    found_product = next((single_product for single_product in products if single_product['id'] == product_id), None)

    if found_product is None:
        abort(404)
    
    return jsonify(found_product)