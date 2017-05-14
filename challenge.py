import urllib
from flask import Flask, json, jsonify, make_response, request, g
import sqlite3
import locale
locale.setlocale(locale.LC_ALL, 'da_DK.UTF-8')


ITEMS_PER_PAGE = 10
DB_NAME = 'products.db'
app = Flask(__name__)


def get_db():
    if not hasattr(g, 'database'):
        g.database = sqlite3.connect(DB_NAME)

        # Allow columns to be accessed by name
        g.database.row_factory = sqlite3.Row
    return g.database


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'database'):
        g.database.close()


@app.route('/products/')
def cheapest_products():
    page = request.args.get('page', 0, type=int)
    start = ITEMS_PER_PAGE * page

    products = execute_db(
        'SELECT * FROM products order by price limit ? offset ?',
        (ITEMS_PER_PAGE, start))

    return jsonify({
        "end-point": request.path,
        "page": page,
        "total": len(products),
        "products": products
    })


@app.route('/products/kids/')
def cheapest_products_kids():
    products = execute_db(
        'SELECT * FROM products WHERE kids = 1 order by price')

    return jsonify({
        "end-point": request.path,
        "products": products
    })


@app.route('/products/<int:product_id>/')
def product_by_id(product_id):
    product = execute_db(
        'SELECT * FROM products WHERE id = ?',
        (product_id,), False)

    if product:
        return jsonify({
            "end-point": request.path,
            "product": product
        })
    else:
        return jsonify({
            "end-point": request.path,
            "product": {}
        }), 404


# Override is needed to return JSON instead of HTML (Flask's default)
@app.errorhandler(404)
def not_found(e):
    error = {"error": "Not found"}
    return make_response(jsonify(error), 404)


# Get data sample from Unisport
def get_data():
    url = "https://www.unisport.dk/api/sample/"
    response = urllib.urlopen(url)
    return json.loads(response.read())


# From point decimal to comma decimal
def to_currency(value):
    return locale.currency(value, False)


# Prepare database result to be jsonified
def handle_db_result(result):
    data = {}

    if(result and len(result) > 0):
        if(type(result[0]) == sqlite3.Row):
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


# Get database result ready for jsonify()
def execute_db(query, values=[], fetchall=True):
    cursor = get_db().cursor()
    cursor.execute(query, values)

    if fetchall:
        return handle_db_result(cursor.fetchall())
    else:
        return handle_db_result(cursor.fetchone())


@app.route('/products/', methods=['POST'])
def create_product():
    pass
