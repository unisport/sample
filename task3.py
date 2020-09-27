import requests
import json

# Setting a base link and extracing all JSON formatted data into the 'data' variable
base_link = 'https://www.unisport.dk/api/products/batch/?list=201338,201481,202483,188894,193858,188896,201176,189188,205946,201450,206348,201440,198079,197237,204692,195932,197362,197250,193638,185253,205962,208030,194885,185256,193539,195935,201174,204085,195606,205949,203906,201337,194925,193652,204086,176719,206385,201447,205896,198575#'
rq = requests.get(base_link)
data = rq.json()
data = data['products']

def paginate_products(d, pagenumber):
  '''Groups products into 10's and returns the batch of products for a particular page'''
  if not(isinstance(pagenumber, int)):
    print(None)
  else:
    if (pagenumber*10) > len(d) + 10:
      print('Page number too high')
    else:
      for product in d[(pagenumber*10)-10 : (pagenumber*10)]:
        product['priceformatted'] = product['price'][:4] + ',' + product['price'][4:]
        print(f"{product['name']} - {product['priceformatted']} DKK")

paginate_products(data, 2)  # example page 2
