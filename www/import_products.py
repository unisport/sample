#!/usr/local/bin/python3
# import requests
import json
# import jsbeautifier
# from pprint import PrettyPrinter

nike_url = 'https://www.unisport.dk/api/products/batch/?list=194477,189187,193599,193602,193601,193592,193574,193575,193593,193595,193573,193572,193576,193579,193571,193580,193581,193591,193596,193590,193594,193584,193589,193582,193583,193577,193587,193569,193585,193578,193588,193570,193586,193600,193537,193541,193465,193466,193539,193443,193455,193468,193445,193480,193459,193462,193536,193540,193538,193542,193453,193479,193467,193464,193446,193473,193457,193476,193447,193469,193461,193477,193450,193472,193454,193474,193449,193471,193458,193475,193448,193470,193460,193478,188530,189213,189217,189211,189212,189033,189214,189188,189032,189216,189034,189215,189035,189037,189031,189036,189052,189056,189057,188819,189054,189044,189046,189053,189058,189045,189047,189049,189048,189055,189059,189060,189051,189061,189050,189062,188541,188549,188910,188906,188827,188554,188912,188899,188820,188527,188946,188967,188832,188548,188823,188833,188824,188531,188736,188909,188956,188826,188908,188930,188926,188904,188907,188916,188905,189221,188931,188927,188835,188550,188915,188955,188901,188551,188968,188834,188546,188921,188932,188933,188919,188959,188830,188924,188918,188836,188934,188928,188552,188547,188917,188831,188923,188935,188929,188960,188920,188964,188943,188936,188553,188837,188937,188941,188957,188950,188969,188958,188942,188951,188972,188952,188947,188962,188948,188970,188944,188965,188973,188963,188939,188971,188949,188966,188945,188954'
nike_url = 'https://www.unisport.dk/api/products/batch/?list=194477'
adidas_url = 'https://www.unisport.dk/api/products/batch/?list=187361,179845,187349,187404,187416,187411,187424,187452,187431,187418,187432,187405,187417,187412,187426,187425,187427,187433,187434,187468,187829,187406,187423,187435,187420,187407,187443,187442,187456,187408,187419,187457,187428,187413,187469,187447,187436,187437,187475,187476'

# response = requests.get(nike_url)
# print(response)
# data = json.dumps(response.json())
# data = jsbeautifier.beautify(data)
# print(data)
# with open('product_sample.json', "w") as file:
#     file.writelines(data)

data = None
with open('product_sample.json', 'r') as file:
    data = json.load(file)

# pp = PrettyPrinter(indent=4)
# pp.pprint(data)

for product in data['products']:
    print(product['id'])
    print(product['attributes']['brand'])
    print(product['name'])
    print(product['image'])
    print(product['url'])
    print(product['price'])
    print(product['currency'])
    print(product['discount_percentage'])
    print(product['delivery'])
    print(','.join([label['name'] for label in product['product_labels']]))
    print(','.join([size['name'] for size in product['stock']]))
    print(','.join(product['attributes']['age']))
    print(','.join(product['attributes']['gender']))

# for product in data['products']:
#     p = Product()
#     p.unisport_id = product['id']
#     p.brand = product['attributes']['brand']
#     p.name = product['name']
#     p.image = product['image']
#     p.url = product['url']
#     p.price = product['price']
#     p.currency = product['currency']
#     p.discount = product['discount_percentage']
#     p.delivery = product['delivery']
#     p.labels = ','.join([label['name'] for label in product['product_labels']])
#     p.sizes = ','.join([size['name'] for size in product['stock']])
#     p.age = product['attributes']['age']
#     p.gender = product['attributes']['gender']
#     p.save()
