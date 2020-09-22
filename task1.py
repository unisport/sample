import requests 
# requests -

rq = requests.get('https://www.unisport.dk/api/products/batch/?list=201338,201481,202483,188894,193858,188896,201176,189188,205946,201450,206348,201440,198079,197237,204692,195932,197362,197250,193638,185253,205962,208030,194885,185256,193539,195935,201174,204085,195606,205949,203906,201337,194925,193652,204086,176719,206385,201447,205896,198575#')
data = rq.json()

# print(type(data)) - printing the type
# print(len(data)) - printing the length
# print(len(data['products']))


# a = {'James': 80, 'Alex': 75}
# print(a['James'])

# b = ['James', 'Alex', 'Matthew']
# b.sort(key=lambda word: word[-1])
# print(b)
#print(b[4])


products = data['products']
products.sort(key=lambda product: product['price'])
# if price.endswith('00'):
#  
# for product in products:
# print('{} has a price of {}'.format(product['name'], product['price']))

cheapest = products[:10]
#priceformatted = price[:3] + ',' + price[3:]
#1459,00
for product in cheapest:
  product['priceformatted'] = product['price'][:4] + ',' + product['price'][4:]
  print(f"{product['name']} - {product['priceformatted']} DKK")




