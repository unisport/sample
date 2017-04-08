import json
import requests as req

from sys import exit
from flask import Flask, request, jsonify

API_URL = "https://www.unisport.dk/api/sample/"
app = Flask(__name__)


def load_data(url):
    """
    Load the sample data and return as json if that is possible.

    Load from the api due the small scale of this project. For larger amounts of data, move data to local database.
    Would also make implementation of bonus features (editing etc.) possible
    """
    response = None
    r = req.get(url)

    if r.status_code != 200:
        print "Failed to load data with HTTP code {}".format(r.status_code)
        return None

    try:
        response = json.loads(r.text)
        return response
    except (TypeError, ValueError):
        print "Returned data seems to be in the wrong format. Recieved:"
        print r.text[:100]
        return None

    return response



data = load_data(API_URL)

#Kill program if we didn't recieve any json
if data is None:
    exit("Try again later")


#Replace commas with decimal points for sorting later on.
#Might be able to change settings to work with commas, but this is probably easier
for p in data['products']:
    p['price'] = float(p['price'].replace(',', '.'))


#Product view. Works with and without the page parameter
@app.route("/products/", methods=["GET"])
def products():
    current_products = data['products'][:10]
    page = request.args.get("page")

    if page is not None:
        index = int(page)*10
        if index < len(data['products']):       
            current_products = data['products'][index: index + 10]
        else:
            return jsonify({"error": "No more products found", "products": []})

    sorted_products = {'products': sorted(current_products, key=lambda k: k['price'])}

    return jsonify(sorted_products)


#View for seeing products for kids
@app.route("/products/kids/", methods=["GET"])
def kids_products():
    current_products = filter(lambda k: k['kids'] == '1', data['products'])
    sorted_products = {'products': sorted(current_products, key=lambda k: k['price'])}

    return jsonify(sorted_products)


#View for seeing a specific product.
@app.route("/products/<id>", methods=["GET"])
def specific_product(id):
    for p in data['products']:
        if p['id'] == id:
            return jsonify(p)

    return jsonify({"error": "Product not found"})


#Run this thing
if __name__ == "__main__":
    app.run()