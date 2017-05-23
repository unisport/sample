import urllib
import json
from models import Product

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
