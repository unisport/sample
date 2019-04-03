'''

Import script for importing the data from the sample site, into a Dict and from the Dict into the DB

I used this in the start untill you altered the data, so made a new import target.

#Importing data into a Dict
url = urllib.request.urlopen("https://www.unisport.dk/api/sample/")
data = json.loads(url.read())

'''

import urllib.request, json
from challenge.models import Product

#Importing data into a Dict
#Reading file
with open('challenge/sample.json', 'r') as filename:
    obj = filename.read()

#Parsing file
data = json.loads(obj)

# Looping through Dict to save the data in the DB
for a in data['products']:
    b = Product()
    if a['kids'] == "1":
        b.kids = True
    else:
        b.kids = False
    if a['kid_adult'] == "1":
        b.kid_adult = True
    else:
        b.kid_adult = False 
    b.name = a['name']
    # Converting the price string to a float and replacing , with . to converting it to a code readable number
    b.price = float(a['price'].replace(',','.'))    
    b.currency = a['currency']
    b.product_id = a['id']
    b.save()