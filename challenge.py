import urllib
from collections import OrderedDict
from flask import Flask, json, jsonify, abort, make_response, request, g
import sqlite3
import locale
locale.setlocale(locale.LC_ALL, 'en_DK.UTF-8')

ITEMS_PER_PAGE = 10
DB_NAME = 'products.db'
app = Flask(__name__)





def get_db():
	if not hasattr(g, 'database'):
		g.database = sqlite3.connect(DB_NAME)
		g.database.row_factory = sqlite3.Row #Allow columns to be accessed by name
	return g.database


@app.teardown_appcontext
def close_db(error):
	if hasattr(g, 'database'):
		g.database.close()

@app.route('/products/')
def cheapest_products():
	page = request.args.get('page', 0, type=int)
	start = ITEMS_PER_PAGE * page
	end = ITEMS_PER_PAGE * (page + 1)

	cursor = get_db().cursor()
	cursor.execute('SELECT * FROM products order by price limit ? offset ?', (ITEMS_PER_PAGE, start))
	
	products = handle_db_result(cursor.fetchall())
	
	return jsonify({
		"end-point": request.path,
		"page": page,
		"total": len(products),
		"products": products
	})
   

@app.route('/products/kids/')
def cheapest_products_kids():
	cursor = get_db().cursor()
	cursor.execute('SELECT * FROM products WHERE kids = 1 order by price')
	
	products = handle_db_result(cursor.fetchall())

	return jsonify({
		"end-point": request.path,
		"products": products
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
	

#Override is needed to return JSON instead of HTML (Flask's default)
@app.errorhandler(404)
def not_found(e):
	error = { "error": "Not found" }
	return make_response(jsonify(error), 404)

#Get data sample from Unisport
def get_data():
	url = "https://www.unisport.dk/api/sample/"
	response = urllib.urlopen(url)
	return json.loads(response.read())

#From point decimal to comma decimal
def to_currency(value):
	return locale.currency(value, False)


#Prepare database result to be jsonified
def handle_db_result(result):
	data = []
	if(len(result) > 1):
		if(type(result[0]) == list):
			data = [dict(i) for i in result]
			for i in data:
				i['id'] = str(i['id'])
				i['price'] = to_currency(i['price'])
				i['price_old'] = to_currency(i['price_old'])
		else:
			data = dict(result)
			data['id'] = str(data['id'])
			data['price'] = to_currency(data['price'])
			data['price_old'] = to_currency(data['price_old'])
	return data
