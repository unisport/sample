import json
from flask import abort, jsonify

"""
Utilities used throughout this fictional domain.
"""


def load_db():
    """
    Loads sample DB from ./static directory.

    :return: Sample database as JSON.
    """
    with open('static/db.json') as data:
        return json.load(data)


def find_product(find: str, value: str):
    """
    Finds product in our sample DB.

    :param find: Key we are searching for.
    :param value: The value that needs to be found.

    :return: Product as JSON object.
    """

    data = load_db()
    found_objects = []

    for product in data['products']:
        if product[f'{find}'] == value:
            found_objects.append(product)
    if not found_objects:
        abort(400, 'Product(s) not found.')
    else:
        return jsonify(found_objects)


def paginate(page: int, items: int = 10):
    """
    DB pagination.

    :param page: Page ID.
    :param items: Amount of products to be returned per page.

    :return: Products.
    """

    data = load_db()
    products = data['products']

    if items is None:
        items = 10

    try:
        chunks = [products[i:i + items] for i in range(0, len(products), items)]

        try:
            next_chunk = chunks[page + 1]
            next_page = page + 1
        except IndexError:
            next_page = 'None'

        return jsonify(chunks[page], {'next_page_id': next_page})
    except IndexError:
        # If requested page ID index is bigger than exists or/ and
        # there are less items than in the client request, the whole product
        # array will be returned.
        return jsonify(data['products'], {'next_page_id': 'None'})


def order_cheapest(items: int = 10):
    """
    Orders products by cheapest price.

    :param items: Amount of products to be returned.

    :return: Products ordered with the cheapest first.
    """

    data = load_db()
    product_list = data['products']

    try:
        chunk = product_list[:items]
        sorted_chunks = sorted(chunk, key=lambda x: int(x['price']), reverse=False)
        return jsonify(sorted_chunks)
    except IndexError:
        return jsonify(sorted(product_list, key=lambda x: int(x['price']), reverse=False))


