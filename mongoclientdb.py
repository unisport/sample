import urllib

import bson
from flask import json
from pymongo import MongoClient
from bson import BSON

url = urllib.request.urlopen("https://www.unisport.dk/api/sample/")
data = json.loads(url.read().decode())

# opretter forbindelsen til mongodb og konverter data til det rigtige format
client = MongoClient()
db = client.test
v1 = data['products']
v2 = json.dumps(v1)
test1 = json.loads(v2)

# indsæt i database, brug foreach så jeg får json objekter istedet for et array

# for test3 in test1:


#  result = db.products.insert_one(test3)
   # ændre typen på price fra string til double
#
#db.products.find().forEach( function (x) {
 #   x.price = parseInt(x.price);
 #   db.products.save(x);
#});

#page værdierne er blevet indsat med robomongo