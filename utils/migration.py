import json

from application import db
from model.product import Product
from schema import ProductSchema


def load_products_attrs(path):
    with open(path, 'r') as jsondb:
        products = json.load(jsondb)['products']
        return products


def migrate(sqlitedb, products):
    for product_attrs in products:
        product = ProductSchema().load(product_attrs).data
        sqlitedb.session.add(Product(**product))
    sqlitedb.session.commit()


if __name__ == '__main__':
    jsondb = load_products_attrs('data.json')
    migrate(db, jsondb)
