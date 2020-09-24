import requests
import json 
# requests -

# /products/?page=2 is not reurning objects (paginated request) since page 1 is
# current API does not provide pagineted request. By the API in line 8 I provided a list as query
# parameter and proving the ID of the products

rq = requests.get('https://www.unisport.dk/api/products/batch/?list=201338')
data = rq.json()
data = data["products"]
for product in data:
  product['priceformatted'] = product['price'][:4] + ',' + product['price'][4:]
  print(f"{product['name']} - {product['priceformatted']} DKK")