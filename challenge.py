import urllib
from collections import OrderedDict
from flask import Flask, json, jsonify, abort, make_response, request
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

CONST_LIMIT = 10

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False #Avoid ordering keys to maintain source's order

@app.route('/products/')
def cheapest_products():
	data = get_data()['products']
	response = None
	
	# /products/?page=n
	if("page" in request.args):
		page = request.args.get("page", -1, type=int)
		start = page * CONST_LIMIT
		
		if(start > len(data) or page == -1):
			abort(404)
			
		end = start + CONST_LIMIT
		if(end > len(data)):
			end = len(data)
		product_list = data[start:end]
		result = {}
		result["products"] = product_list
		response = jsonify(result)
	#/products/
	else:
		products = order_by_price(data)
		result = {}
		product_list = []
		
		for i in range(0, CONST_LIMIT):
			product_list.append(products[i])
	
		result["products"] = product_list
		response = jsonify(result)
	
	return response
   

@app.route('/products/kids/')
def cheapest_products_kids():
	products = order_by_price(get_kid_products()['products'])
	if(len(products) == 0):
		abort(404)
		
	return jsonify(products)

@app.route('/products/<int:product_id>/')
def product_by_id(product_id):
	data = get_data()['products']
	result = {}
	product = {}
	found = False
	i = 0
	while (i < len(data) and not found):
		if(data[i]["id"] == product_id):
			product = data[i]
			found = True
		i += 1
	
	if(not found):
		abort(404)
	
	result["product"] = product
	response = jsonify(result)
	
	
	return response


#Override is needed to return json instead of HTML (Flask's default)
@app.errorhandler(404)
def not_found(e):
	error = { "error": "Not found" }
	return make_response(jsonify(error), 404)


def get_kid_products():
	data = get_data()['products']
	product_list = []
	result = {}
	for i in range(0, len(data)):
		if(data[i]["kids"] == "1"):
			product_list.append(data[i])
	
	result["products"] = product_list
        return result

#Get data sample from Unisport
def get_data():
	#url = "https://www.unisport.dk/api/sample/"
	url = "http://paste.debian.net/plainh/c838890c"
	response = urllib.urlopen(url)
	return json.loads(response.read(), object_pairs_hook=OrderedDict) #Maintain keys order

def currency_to_float(currency_str):
	return locale.atof(currency_str)
        
#Set order to True for descending order. Ascending otherwise.
def order_by_price(data, order=False):
	return sorted(data, key=lambda k: currency_to_float(k['price']), reverse=order)