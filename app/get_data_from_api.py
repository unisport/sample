import requests
import pandas as pd
import json


#Requests data from the API if possible.
def request_api():
    try:
        r = requests.get('https://www.unisport.dk/api/sample/')
        data = json.loads(r.text)['products']
    except Exception:
        pass
    return data


#Selecting the needed products from the api and saving them as a dict in the list "products".
products = []

for i in request_api():
    d = {}
    d['name'] = i['name']
    d['price'] = i['price']
    d['image'] = i['image']

    products.append(d)


#Creating a pandas dataframe and exporting the data to csv.
df = pd.DataFrame(products)
df.to_csv('static/csv/products.csv')

