# -*- coding: utf-8 -*-
import web
from models import *
import json
import pdb
import logging

urls = (
    '/hello_kitty', 'BadKitty',
    '/products/', 'Products',
    '/product/(.+)/', 'LeProduit',
    '/products/kids/', 'ProductKids'
)

app = web.application(urls, globals())


class BadKitty:
    """
    This class is just to ensure everything
    has been setup correctly
    """
    def GET(self):
        web.header('Content-Type', 'text/html')
        return 'Hello, Kitty'


class Products:
    """
    Fetch a list of products from the database and
    sort them based on lowest price first
    Return the 10 first items in the list as json
    with the proper Content type
    """
    def GET(self):
        data = web.input(page=1)
        page = int(data.page)

        products = Product.select().order_by(
                Product.price.asc()).paginate(page, 10)
        product_list = []
        for product in products[0:10]:
            product_list.append(model_to_dict(product))

        web.header('Content-Type', 'applicatino/json')
        return json.dumps(product_list)


class ProductKids:
    """
    Select all products where kids = True and return
    these sorted by lowest price first
    """
    def GET(self):
        products = Product.select().where(
                Product.for_kids == True).order_by(Product.price.asc())

        web.header('Content-Type', 'application/json')
        product_list = []
        for product in products:
            product_list.append(model_to_dict(product))

        return json.dumps(product_list)


class LeProduit:
    """
    Why french? why not, n'est pas?
    Part of the URL holds a reference to a product_id.
    The product_id is used to get the matching product from the database
    which is then returned as json
    """
    def GET(self, product_id):
        try:
            product = Product.get(Product.product_id == product_id)
        except DoesNotExist:
            raise web.seeother('/404/')

        web.header('Content-Type', 'application/json')
        return json.dumps(model_to_dict(product))


if __name__ == '__main__':
    app.run()
