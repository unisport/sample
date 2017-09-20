"""
main.py - Unisport Sample webservice

The general layout and semantic of the application is generalized where I thought possible,
    and put into context of each endpoint.
This is done to further the understanding of the process the data goes through,
    which is very much the same at each endpoint.

The endpoints are:
/products
/products/kids
/products/<id>

The endpoints /products and /products/kids also have the ability the take in a page query-parameter,
    which will return the requested page, if it exists, e.g: /products?page=2
All the endpoints will 404, if any query or request is validated falsy.
This is done because I believe standard 404 errors should be a part of a standard API design.

I believe the specific requirements of the web service have been met.
The original repo and said requirements can be found here: https://github.com/unisport/sample

Extra:

If I would have had more time on my hands, I would've implemented a SQLAlchemy model Product(),
which would serve as a backend connection. I would then make a RESTful implementation of the webservice.
This way any user of the web service API could create, read, update, and delete products as they would see fit.
This could further be extended to use some kind of frontend framework, which would handle these requests.
Or you could use XHR. Or even another server, which would serve pages with forms to edit and delete products, etc.

"""

import json
from flask import Flask, jsonify, request, abort
# from requests import get # Easy-to-use function. No hassle with it. Would be used, if data was gotten dynamically

from utilities import paginate, parse_money # Self-made utility functions

app = Flask(__name__)

@app.route("/products")
def products():
    """
    The /products endpoint. The is made as per the design request.
    """

    # Query-parameter as per the design request of the web service api
    selected_page = request.args.get("page")
    products_list = data["products"]
    sorted_products = sorted(products_list, key=lambda p: parse_money(p["price"], p["currency"]))
    pages = paginate(sorted_products, 10)

    # I didn't a user of the web service to have to specify a page number,
    # if he/she only wants the first page.
    if selected_page is None:
        cheapest_products = pages[0]
    else:
        # Throw a 404, if page doesn't exist. This is done as per the design request.
        if int(selected_page) > len(pages):
            abort(404)
        # Return the queried page.
        cheapest_products = pages[int(selected_page) - 1]
    
    return jsonify(cheapest_products)

@app.route("/products/kids")
def kids_products():
    """
    The /products/kids endpoint. The is made as per the design request.
    Will 404, if queried page doesn't exist.
    """

    # Accept a page query-parameter. This done as per the design request.
    selected_page = request.args.get("page")

    # I try to use set builder notation, because it's dense and mathematical.
    products_list = [p for p in data["products"] if p["kids"] == "1"]

    # I used the built-in sorting method because of easy accessibility.
    # It also provides a nice feature for sorting by a specified key.
    sorted_products = sorted(products_list, key=lambda p: parse_money(p["price"], p["currency"])) 

    pages = paginate(sorted_products, 10)

    if selected_page is None:
        cheapest_products = pages[0]
    else:
        if int(selected_page) > len(pages):
            abort(404)
        cheapest_products = pages[int(selected_page) - 1]
    
    return jsonify(cheapest_products)

@app.route("/products/<_id>")
def product_by_id(_id):
    """
    The /products/<_id> endpoint. This is made as per the design request.
    Will 404, if the requested id is not found.
    """
    products_list = data["products"]
    for p in products_list: # Linearly search the products-list. This is done for simplicity.
        if p["id"] == _id:
            return jsonify(p)
    abort(404)

if __name__ == "__main__":
    # Data last updated: 19-09-2017 18:05
    # The data is a constant in this case, because of unit testing.
    # Another way would be to dynamically get the data with
    # requests.get("https://www.unisport.dk/api/sample").json()
    #
    # The data is set at the beginning, because the data is more-or-less static.
    # I find no need to get the data every time a call is made to a route.
    with open("data.json", encoding="utf8") as input_data:
        data = json.load(input_data)
        app.run(debug=True)
