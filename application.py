from flask import request

from config import app
from model.product import Product
from schema import ProductSchema


@app.route('/products/', methods=['GET'])
def products():
    with app.app_context():
        page = int(request.args.get('page', 1))
        items = Product.query.order_by(Product.price).all()
        return ProductSchema().dump(items[10 * (page-1):10 * page], many=True)


@app.route('/products/kids', methods=['GET'])
def kids():
    with app.app_context():
        items = Product.query.filter(Product.kids == '1').order_by(Product.price).all()
        return ProductSchema().dump(items, many=True)


if __name__ == '__main__':
    app.run()
