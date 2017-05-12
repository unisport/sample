import urllib
from collections import OrderedDict
from flask import Flask, json, jsonify, abort, make_response, request
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

ITEMS_PER_PAGE = 10

app = Flask(__name__)

@app.route('/products/')
def cheapest_products():
	page = request.args.get('page', 0, type=int)
	products = order_by_price(get_data()['products'])
	start = ITEMS_PER_PAGE * page
	end = ITEMS_PER_PAGE * (page + 1)
	
	return jsonify({
		"end-point": request.path,
		"page": page,
		"total": len(products),
		"products": products[start:end]
	})

   

@app.route('/products/kids/')
def cheapest_products_kids():
	products = get_data()['products']
	kid_products = [product for product in products if product['kids'] == '1']

	return jsonify({
		"end-point": request.path,
		"products": order_by_price(kid_products)
	})

@app.route('/products/<int:product_id>/')
def product_by_id(product_id):
	products = get_data()['products']
	product = [product for product in products if int(product['id']) == product_id]
	
	if product:
		return jsonify({
			"end-point": request.path,
			"product": product[0]
		})
	else:
		return jsonify({
			"end-point": request.path,
			"product": {}
		}), 404
	

#Override is needed to return json instead of HTML (Flask's default)
@app.errorhandler(404)
def not_found(e):
	error = { "error": "Not found" }
	return make_response(jsonify(error), 404)

#Get data sample from Unisport
def get_data():
	#url = "https://www.unisport.dk/api/sample/"
	url = "http://paste.debian.net/plainh/c838890c"
	response = urllib.urlopen(url)
	return json.loads(response.read())

def currency_to_float(currency_str):
	return locale.atof(currency_str)
        
#Set order to True for descending order. Ascending otherwise.
def order_by_price(data, order=False):
	return sorted(data, key=lambda k: currency_to_float(k['price']), reverse=order)