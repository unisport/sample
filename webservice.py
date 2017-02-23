import web
from models import *
import json
import pdb
import logging

urls = (
    '/hello_kitty', 'BadKitty',
    '/products/', 'Products',
    '/product/(.+)/', 'LeProduit',
    '/products/(.+)', 'ProductPager'
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
        products = Product.select().order_by(Product.price.asc())
        product_list = []
        for product in products[0:10]:
            product_list.append(model_to_dict(product))

        web.header('Content-Type', 'applicatino/json')
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


class ProductPager:
    """
    Here peewee's built-in paginater is used to get
    the required number of results, these are then returned as json
    """
    def GET(self, page):
        products = Product.select().paginate(int(page), 10)
        product_list = []
        for product in products:
            product_list.append(model_to_dict(product))

        web.header('Content-Type', 'application/json')
        return json.dumps(product_list)


if __name__ == '__main__':
    app.run()
