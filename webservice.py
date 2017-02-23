import web
from models import *
import json
import pdb

urls = (
    '/hello_kitty', 'BadKitty',
    '/products/', 'Products',
    '/product/(.+)/', 'LeProduit'
)

app = web.application(urls, globals())


class BadKitty:
    def GET(self):
        web.header('Content-Type', 'text/html')
        return 'Hello, Kitty'


class Products:
    def GET(self):
        web.header('Content-Type', 'applicatino/json')
        # pdb.set_trace()
        products = Product.select().order_by(Product.price.desc())
        product_list = []
        for product in products[0:10]:
            product_list.append(model_to_dict(product))

        return json.dumps(product_list)


class LeProduit:
    def GET(self, product_id):
        try:
            product = Product.get(Product.product_id == product_id)
        except DoesNotExist:
            raise web.seeother('/404/')

        web.header('Content-Type', 'application/json')
        return json.dumps(model_to_dict(product))


if __name__ == '__main__':
    app.run()
