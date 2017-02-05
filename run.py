#!/usr/bin/env python3

import urllib.request
import json
from flask import Flask
from flask import jsonify
from flask import request

data = {}
app = Flask(__name__)

"""
General remarks:
--------------
I have chosen to just return json objects.
If the webservice is for customers to see, you could improve the
UX by using Jinja2 templates to show the objects nicely.
"""


@app.route("/products/")
def products():
    """
    Gets the sorted products data (see function)
    Since we want page to start at page 1 (and not page 0),
    we have to subtract 1 from page if page is larger than 0.
    The reason is, that we want to start from index 0, at page 1
    We asume that we also want page 1 if page is 0 (or less).

    Further improvement could be a error message
    if page is less than 0 (or maybe 0)
    """
    page = request.args.get('page')
    sorted_data = get_sorted_products_by_price()
    if not page or int(page) <= 0:
        page = 0
    else:
        page = int(page)-1
    return jsonify(sorted_data["products"][10*page:10*(page+1)])


@app.route("/products/<int:id_number>")
def products_id(id_number):
    """
    Since we know that id_number is an integer,
    we tell Flask this in its routing and use it for finding the product id.
    """
    return jsonify([x for x in data["products"] if int(x["id"]) == id_number])


@app.route("/products/kids")
def products_kids():
    """
    We re-use the sorting function and return the wanted products
    """
    kids_data = get_sorted_products_by_price()
    return jsonify([item for item in kids_data['products']
                    if int(item['kids']) == 1])


def load_data():
    """
    We fetch the data and save the json in memory as a dictonary.
    Íf the data was much bigger, then we want to search for it,
    in a more persistence data-store, like MongoDB

    A more persistence data-store, would make sence if you implement
    save, edit, delete methods of data (Bonus task)
    If we asume the json structure, then MongoDB will be an excellent choice,
    since the structure would be more or less the same
    """
    url = "https://www.unisport.dk/api/sample/"
    data = urllib.request.urlopen(url)
    return json.loads(data.read().decode("utf8"))


def get_sorted_products_by_price(reverse=False):
    """
    Since we need to convert the price values to float type so we can sort
    the products by the price, ("1.600,50" --> 1600.50),
    we use a lambda function to make the conversion,
    and use it in the "sorted" function in the "key" parameter.

    We have added an parameter, so we easily can choose in which ordering
    the sorting should give us.
    OBS: Not necessary in this task, but could be handy
    """
    return {
        "products":
            sorted(
                data["products"],
                key=lambda x: float(x["price"].strip(".").replace(",", ".")),
                reverse=reverse
            )
    }


if __name__ == '__main__':
    data = load_data()  # Loading the data at startup, so we have it in memory
    app.run(debug=False)
