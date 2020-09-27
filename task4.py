import requests
import json

# Setting a base link and extracing all JSON formatted data into the 'data' variable
base_link = 'https://www.unisport.dk/api/products/batch/?list=201338,201481,202483,188894,193858,188896,201176,189188,205946,201450,206348,201440,198079,197237,204692,195932,197362,197250,193638,185253,205962,208030,194885,185256,193539,195935,201174,204085,195606,205949,203906,201337,194925,193652,204086,176719,206385,201447,205896,198575#'
rq = requests.get(base_link)
data = rq.json()
data = data['products']

def return_product_ids():
    '''Returns all product ids - Used as a facilty function to check id's are valid'''
    return [i['id'] for i in data]


def return_specific_product(d, id):
    '''Returns individual product based off the ID'''
    if id not in return_product_ids():
        print('No such item found')
    else:
        print(''.join([i['name'] for i in data if i['id'] == id]))

return_specific_product(data, '201338')   # example with the first valid ID