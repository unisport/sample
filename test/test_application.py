import flask

from config import db
from test.helpers.decorators import create_db, instance
from test.helpers.utils import add_product


@create_db
def test_should_fetch_first_10_products_in_asc_order():
    EXPECTED_LENGTH = 10
    for i in range(1, 20):
        product = {'id': i, 'name': 'Some product', 'price': 1000 - 5*i}
        add_product(db, **product)
    with instance.application.app_context():
        response = instance.get('/products')
        products = flask.json.loads(response.data)
        assert len(products) == EXPECTED_LENGTH
        assert all(products[i]['price'] <= products[i+1]['price'] for i in range(EXPECTED_LENGTH-1))


@create_db
def test_returns_products_for_kids():
    EXPECTED_LENGTH = 2
    add_product(db, id=1, kids=1, name='Some product', price=500)
    add_product(db, id=2, kids=0, name='Some product', price=450)
    add_product(db, id=3, kids=0, name='Some product', price=300)
    add_product(db, id=4, kids=1, name='Some product', price=100)
    with instance.application.app_context():
        response = instance.get('/products/kids')
        products = flask.json.loads(response.data)
        assert len(products) == EXPECTED_LENGTH
        assert all(products[i]['price'] <= products[i + 1]['price'] for i in range(len(products)-1))
