import urllib
import json
from locale import atof

# fetch all products
def get_products():
    response = urllib.urlopen("https://www.unisport.dk/api/sample/")
    data = json.loads(response.read())

    return data["products"]

# fetch all products ordered by price in ascending order
def get_products_ordered_by_price():
    products = get_products()

    # convert each price string to float based key value
    # for better sortability
    return sorted(products, key=lambda k: atof(k["price"]))

# fetch all kids products
def get_kids_products():
    products = get_products_ordered_by_price()

    return [product for product in products if product["kids"] == "1"]

# fetch a product by the specified id
def get_product(id):
    products = get_products()
    iterator = (product for product in products if int(product["id"]) == id)

    product = next(iterator, None)

    return product
