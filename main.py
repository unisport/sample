"""
main.py - Unisport Sample webservice
"""

from flask import Flask, jsonify, request, abort
from requests import get

from utilities import paginate, parse_money

app = Flask(__name__)

@app.route("/products")
def products():
    """
    :returns: the top 10 cheapest products.
    """
    selected_page = request.args.get("page")
    products_list = data["products"]
    sorted_products = sorted(products_list, key=lambda p: parse_money(p["price"], p["currency"]))
    pages = paginate(sorted_products, 10)

    if selected_page is None:
        cheapest_products = pages[0]
    else:
        if int(selected_page) > len(pages):
            abort(404)
        cheapest_products = pages[int(selected_page) - 1]
    
    return jsonify(cheapest_products)

@app.route("/products/kids")
def kids_products():
    """
    :returns: kids products ordered by price.
    """
    selected_page = request.args.get("page")
    products_list = [p for p in data["products"] if p["kids"] == "1"]
    sorted_products = sorted(products_list, key=lambda p: parse_money(p["price"], p["currency"]))
    pages = paginate(sorted_products, 10)

    if selected_page is None:
        cheapest_products = pages[0]
    else:
        if int(selected_page) > len(pages):
            abort(404)
        cheapest_products = pages[int(selected_page) - 1]
    
    return jsonify(cheapest_products)

@app.route("/products/<id>")
def product_by_id(id):
    products_list = data["products"]
    for p in products_list:
        if p["id"] == id:
            return jsonify(p)
    abort(404)

if __name__ == "__main__":
    data = get("https://www.unisport.dk/api/sample/").json()
    app.run(debug=True)
