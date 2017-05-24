import urllib
import json
from models import Product
from unisport import db
from seeder import format_price, string_bit_to_boolean


# fetch all products
def get_products():
    result = Product.query.all()
    products = [product.as_dict() for product in result]

    return products


# fetch all products ordered by price in ascending order
def get_products_ordered_by_price():
    result = Product.query.order_by(
        Product.price.asc()
    ).all()

    return [product.as_dict() for product in result]


# fetch all kids products
def get_kids_products():
    result = Product.query.filter(
        Product.kids == 1
    ).order_by(
        Product.price.asc()
    ).all()

    return [product.as_dict() for product in result]


# fetch a product by the specified id
def get_product(id):
    product = Product.query.get(id)

    if product is None:
        return product

    return product.as_dict()


# create new product
def create_product(product):
    db.session.add(product)
    db.session.commit()
    db.session.rollback()

    return product.as_dict()


# updates a product based the specified id
def update_product(id, data):
    product = Product.query.get(id)

    product.name = data["name"]
    product.delivery = data['delivery']
    product.free_porto = string_bit_to_boolean(data['free_porto'])
    product.img_url = data['img_url']
    product.kid_adult = string_bit_to_boolean(data['kid_adult'])
    product.kids = string_bit_to_boolean(data['kids'])
    product.package = string_bit_to_boolean(data['package'])
    product.price = format_price(data['price'])
    product.price_old = format_price(data['price_old'])
    product.sizes = data['sizes']
    product.url = data['url']
    product.women = string_bit_to_boolean(data['women'])

    db.session.add(product)
    db.session.commit()
    db.session.rollback()

    return product.as_dict()


# deletes a product with the specified id
def delete_product(id):
    product = Product.query.get(id)

    db.session.delete(product)
    db.session.commit()
