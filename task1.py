import requests
import json

# Setting a base link and extracing all JSON formatted data into the 'data' variable
base_link = 'https://www.unisport.dk/api/products/batch/?list=201338,201481,202483,188894,193858,188896,201176,189188,205946,201450,206348,201440,198079,197237,204692,195932,197362,197250,193638,185253,205962,208030,194885,185256,193539,195935,201174,204085,195606,205949,203906,201337,194925,193652,204086,176719,206385,201447,205896,198575#'
rq = requests.get(base_link)
data = rq.json()
data = data['products']

def show_first_10_products(d):
    #Extracts only first 10 products, then applies a lambda to sort by price'''
    first_ten_products = d[:10]
    first_ten_products.sort(key=lambda product: product["price"])

    for product in first_ten_products:
      product['priceformatted'] = product['price'][:4] + ',' + product['price'][4:]
      print(f"{product['name']} - {product['priceformatted']} DKK")


show_first_10_products(data) 