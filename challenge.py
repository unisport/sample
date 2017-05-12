import urllib
from collections import OrderedDict
from flask import Flask, json, jsonify, abort, make_response
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

CONST_LIMIT = 10

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False #Avoid ordering keys to maintain source's order

@app.route('/products/')
def cheapest_products():
	data = get_data()['products']
	products = sorted(data, key=lambda k: currency_to_float(k['price']))
	result = {}
	product_list = []
	for i in range(0, CONST_LIMIT):
		product_list.append(products[i])
	result['products'] = product_list
	return jsonify(result)
   

@app.route('/products/kids/')
def cheapest_products_kids():
	products = order_by_price(get_kid_products()['products'])
	if(len(products) == 0):
		abort(404)
		
	return jsonify(products)


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
	url = "https://www.unisport.dk/api/sample/"
	response = urllib.urlopen(url)
	return json.loads(response.read(), object_pairs_hook=OrderedDict) #Maintain keys order

def currency_to_float(currency_str):
	return locale.atof(currency_str)
        
#Set order to True for descending order. Ascending otherwise.
def order_by_price(data, order=False):
	return sorted(data, key=lambda k: currency_to_float(k['price']), reverse=order)