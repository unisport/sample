import requests
import json 
# requests -

rq = requests.get('https://www.unisport.dk/api/products/batch/?list=201338,201481,202483,188894,193858,188896,201176,189188,205946,201450,206348,201440,198079,197237,204692,195932,197362,197250,193638,185253,205962,208030,194885,185256,193539,195935,201174,204085,195606,205949,203906,201337,194925,193652,204086,176719,206385,201447,205896,198575#')
data = rq.json()

data = data['products']
data_kids = [product for product in data if "kids" in product["attributes"]["age"]]
print(len(data_kids)) #there are no kids present in the data
data_adults = [product for product in data if "Adults" in product["attributes"]["age"]]
data_adults.sort(key=lambda x: x["price"])
for product in data_adults:
  product['priceformatted'] = product['price'][:4] + ',' + product['price'][4:]
  print(f"{product['name']} for {' '.join(product['attributes']['age'])} - {product['priceformatted']} DKK")



