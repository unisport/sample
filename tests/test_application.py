import flask

from config import db
from tests.helpers.decorators import create_db, instance
from tests.helpers.utils import add_product


@create_db
def test_should_fetch_first_10_products_in_asc_order():
    EXPECTED_LENGTH = 10
    for i in range(1, 20):
        product = {'id': i, 'name': 'Some product', 'price': 1000 - 5*i}
        add_product(db, **product)
    with instance.application.app_context():
        response = instance.get('/products/')
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


@create_db
def test_pagination_on_valid_pages():
    EXPECTED_LENGTH = 10
    for i in range(1, 21):
        product = {'id': i, 'name': 'Some product', 'price': 10 * i}
        add_product(db, **product)
    with instance.application.app_context():
        response = instance.get('/products/?page=1')
        products = flask.json.loads(response.data)
        assert len(products) == EXPECTED_LENGTH
        for i in range(10):
            assert products[i]['id'] == i + 1

        response = instance.get('/products/?page=2')
        products = flask.json.loads(response.data)
        assert len(products) == EXPECTED_LENGTH
        for i in range(10):
            assert products[i]['id'] == i + 11


@create_db
def test_pagination_on_invalid_pages():
    EXPECTED_LENGTH = 10
    for i in range(1, 21):
        product = {'id': i, 'name': 'Some product', 'price': 10 * i}
        add_product(db, **product)
    with instance.application.app_context():
        response = instance.get('/products/?page=GARBAGE')
        products = flask.json.loads(response.data)
        assert len(products) == EXPECTED_LENGTH
        for i in range(10):
            assert products[i]['id'] == i + 1


@create_db
def test_fetch_product_by_valid_id():
    product = {'id': 42, 'name': 'Some product', 'price': 10.0}
    add_product(db, **product)
    with instance.application.app_context():
        response = instance.get('/products/42/')
        product = flask.json.loads(response.data)
        assert product['id'] == 42
        assert product['name'] == 'Some product'
        assert float(product['price']) == 10.0


@create_db
def test_fetch_non_existent_product():
    product = {'id': 42, 'name': 'Some product', 'price': 10.0}
    add_product(db, **product)
    with instance.application.app_context():
        response = instance.get('/products/100500/')
        product = flask.json.loads(response.data)
        assert product == {}


@create_db
def test_fetch_product_with_non_valid_id():
    product = {'id': 42, 'name': 'Some product', 'price': 10.0}
    add_product(db, **product)
    with instance.application.app_context():
        response = instance.get('/products/GARBAGE/')
        product = flask.json.loads(response.data)
        assert product == {}
