import urllib
import data as data
import lines as lines
import mongo as mongo
from flask import Flask, json, jsonify, request, render_template
from pip._vendor import requests
from bson.json_util import dumps
import urllib.request
import random
import sys
import os
from pymongo import MongoClient
from flask_pymongo import PyMongo

client = MongoClient()
db = client.test

app = Flask(__name__)

mongo = PyMongo(app)

# webservicen er blevet testet med postman https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop

# hello world
@app.route('/')
def hello_world():

    return "hello world"

# vis de billigste produkter, hvor mak grænsen er 10
@app.route('/products/', methods=['GET'] )
def products():
    test = db.products
    test4 = test.find().limit(10).sort("price",1)
    return dumps(test4)

# vis de billigste produkter, for børn hvor max grænsen er 10
@app.route('/products/kids/')
def productskids():
    test = db.products
    test4 = test.find({"kids": "1"}).limit(10).sort("price", 1)
    return dumps(test4)

# paginated
@app.route('/products/?<page>/')
def page(page):
    test = db.products
    test4 = test.find({"page": page})
    return dumps(test4)


# find id
@app.route('/products/<id>/')
def idproducts(id):
      test = db.products
      test4 = test.find({"id": id})
      return dumps(test4)



if __name__ == '__main__':
    app.run(debug=True)
