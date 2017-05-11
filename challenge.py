import urllib
from collections import OrderedDict
from flask import Flask, json, jsonify

CONST_LIMIT = 10

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False #Avoid ordering keys to maintain source's order

@app.route('/products/')
def cheapest_products():
	data = get_data()['products']
	products = sorted(data, key=lambda k: international_float(k['price']))
	result = {}
	product_list = []
	for i in range(0, CONST_LIMIT):
		product_list.append(products[i])
	result['products'] = product_list
	return jsonify(result)
    
    
    
#Get data sample from Unisport
def get_data():
	url = "https://www.unisport.dk/api/sample/"
	response = urllib.urlopen(url)
	return json.loads(response.read(), object_pairs_hook=OrderedDict) #Maintain keys order

#Converts a string that represents a comma decimal into a point decimal
def international_float(string_number):
	string_number = string_number.replace('.', '')
	string_number = string_number.replace(',', '.')
	number = float(string_number)
	return number 