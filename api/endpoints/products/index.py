from flask import Blueprint, request, abort

from ....util.product_functions import find_product, paginate, order_cheapest

"""
I've divided everything down into smaller components/ layers, but 
because I'm only implementing two endpoints, I've decided to put both functions under one roof. 

Also, I'm not using OOP as the functionality is not that complex and can be easily achieved with FP.
"""

products = Blueprint('products', __name__, url_prefix='/products')


@products.route('/', methods=['GET'])
def filter_products():
    page = request.args.get('page', type=int)
    # Specify how many objects needs to be returned (defaults to 10).
    items = request.args.get('items', type=int)
    if page:
        return paginate(page=page, items=items)
    else:
        return order_cheapest(items)


@products.route('/id', methods=['GET'])
def get_products():
    product = request.args.get('product', type=str)
    if not product:
        abort(404, 'Product ID was not provided by the client.')
    else:
        return find_product(find='id', value=product)
