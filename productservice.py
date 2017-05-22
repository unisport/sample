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
