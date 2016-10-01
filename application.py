from flask import request

from config import app
from model.product import Product
from schema import ProductSchema, PageSchema, ValidationException

PAGE_SIZE = 10


@app.route('/products/', methods=['GET'])
def products():
    with app.app_context():
        try:
            page = PageSchema().load(request.args).data.get('page', 1)
        except ValidationException:
            page = 1
        items = Product.query.order_by(Product.price).all()
        begin = PAGE_SIZE * (page - 1)
        end = PAGE_SIZE * page
        return ProductSchema().dump(items[begin:end], many=True)


@app.route('/products/kids', methods=['GET'])
def kids():
    with app.app_context():
        items = Product.query.filter(Product.kids == '1').order_by(Product.price).all()
        return ProductSchema().dump(items, many=True)


if __name__ == '__main__':
    app.run()
