import logging
from logging.handlers import RotatingFileHandler

from flask import render_template, request, redirect

from config import app, db
from models.product import Product
from schema import ProductSchema, PageSchema, ValidationException, ProductIdSchema

PAGE_SIZE = 10


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/products/', methods=['GET'])
def products():
    try:
        page = PageSchema().load(request.args).data.get('page', 1)
    except ValidationException:
        app.logger.exception('Someone tries to send non-valid page')
        page = 1
    items = Product.query.order_by(Product.price).all()
    begin = PAGE_SIZE * (page - 1)
    end = PAGE_SIZE * page
    result = ProductSchema().dump(items[begin:end], many=True).data
    return render_template('products_list.html', items=result)


@app.route('/products/<prod_id>/', methods=['GET'])
def product(prod_id):
    try:
        checked_prod_id = ProductIdSchema().load({'prod_id': prod_id}).data['prod_id']
        item = Product.query.filter(Product.id == checked_prod_id).one()
    except (ValidationException, Exception):
        app.logger.exception('Someone tries to send non-valid product id: {}'.format(prod_id))
        return redirect('/products/', code=400)
    return render_template('product_details.html', item=ProductSchema().dump(item).data)


@app.route('/product/', methods=['GET', 'POST'])
def manage_product():
    if request.method == 'POST':
        item = ProductSchema().load(request.form.to_dict()).data
        db.session.add(Product(**item))
        db.session.commit()
        return redirect('/', code=302)
    else:
        return render_template('create_product.html')


@app.route('/update-product/<prod_id>/', methods=['PUT'])
def update_product(prod_id):
    try:
        checked_prod_id = ProductIdSchema().load({'prod_id': prod_id}).data['prod_id']
        item_data = ProductSchema().load(request.form.to_dict()).data
        Product.query.filter_by(id=checked_prod_id).update(item_data)
        db.session.commit()
    except (ValidationException, Exception):
        app.logger.exception('Someone tries to send non-valid product id: {}'.format(prod_id))
        return redirect('/', code=400)
    return "200"


@app.route('/product/<prod_id>/', methods=['DELETE'])
def delete_product(prod_id=None):
    try:
        checked_prod_id = ProductIdSchema().load({'prod_id': prod_id}).data['prod_id']
        item = Product.query.get(checked_prod_id)
        db.session.delete(item)
        db.session.commit()
    except (ValidationException, Exception):
        app.logger.exception('Someone tries to send non-valid product id: {}'.format(prod_id))
        return redirect('/', code=400)
    return redirect('/', code=200)


@app.route('/products/kids/', methods=['GET'])
def kids():
    items = Product.query.filter(Product.kids == '1').order_by(Product.price).all()
    items = ProductSchema().dump(items, many=True).data
    return render_template('products_list.html', items=items)


if __name__ == '__main__':
    handler = RotatingFileHandler('logging.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)
    app.run()
