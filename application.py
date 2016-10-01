import logging
from logging.handlers import RotatingFileHandler

import flask
from flask import render_template
from flask import request

from config import app
from model.product import Product
from schema import ProductSchema, PageSchema, ValidationException, ProductIdSchema

PAGE_SIZE = 10


@app.route('/products/', methods=['GET'])
def products():
    with app.app_context():
        try:
            page = PageSchema().load(request.args).data.get('page', 1)
        except ValidationException:
            app.logger.exception('Someone tries to send non-valid page')
            page = 1
        items = Product.query.order_by(Product.price).all()
        begin = PAGE_SIZE * (page - 1)
        end = PAGE_SIZE * page
        items = ProductSchema().dump(items[begin:end], many=True)
        return render_template('index.html', items=items)


@app.route('/products/<prod_id>/', methods=['GET'])
def product(prod_id):
    try:
        checked_prod_id = ProductIdSchema().load({'prod_id': prod_id}).data['prod_id']
        item = Product.query.filter(Product.id == checked_prod_id).one()
    except (ValidationException, Exception):
        app.logger.exception('Someone tries to send non-valid product id: {}'.format(prod_id))
        return flask.jsonify({})
    return ProductSchema().dump(item).data


@app.route('/products/kids', methods=['GET'])
def kids():
    with app.app_context():
        items = Product.query.filter(Product.kids == '1').order_by(Product.price).all()
        return ProductSchema().dump(items, many=True)


if __name__ == '__main__':
    handler = RotatingFileHandler('logging.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)
    app.run()
