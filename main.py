from flask import Flask, jsonify
from requests import get
from money import Money
from re import match

app = Flask(__name__)

"""
Parses a money-amount based on its value and currency-type.

:param s: the value of the money
:param c: the currency-type of the money
:returns: Money(s, c)
"""
def parse_money(s, c):
    if match(".+(\.|,)00", s):
        return Money(s[:-3], c)
    return Money(s, c)

@app.route("/products")
def products():
    products_list = data["products"]
    cheapest_products = sorted(products_list, key=lambda p: parse_money(p["price"], p["currency"]))[:10]

    return jsonify(cheapest_products)

@app.route("/products/kids")
def kids_products():
    kids_products_list = [p for p in data["products"] if p["kid_adult"] == "1"]
    cheapest_kids_products = sorted(kids_products_list, key=lambda p: parse_money(p["price"], p["currency"]))

    return jsonify(cheapest_kids_products)

if __name__ == "__main__":
    data = get("https://www.unisport.dk/api/sample/").json()
    app.run(debug=True)
