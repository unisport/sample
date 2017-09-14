"""
main.py - Unisport Sample webservice
"""

from re import match

from flask import Flask, jsonify, request, abort
from requests import get
from money import Money

app = Flask(__name__)

def paginate(items, page_size):
    """
    Paginates a list.

    :param items: the items to paginate.
    :param page_size: the size of each page.
    :returns: the paginated items-list, where each page is size of page_size.
    """
    pages = []
    start = 0
    end = 0
    for i in range(len(items)):
        end = i + page_size
        if i % page_size == 0:
            page = items[start:end]
            pages.append(page)
            start = end
    return pages

def parse_money(value, currency):
    """
    Parses a money-amount based on its value and currency-type.

    :param value: the value of the money-amount
    :param currency: the currency-type of the money
    :returns: Money(value, currency)
    """
    if match(r".+(\.|,)00$", value):
        return Money(value[:-3], currency)
    return Money(value, currency)

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
    products_list = [p for p in data["products"] if p["kid_adult"] == "1"]
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
