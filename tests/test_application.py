import logging

from config import db
from models.product import Product
from tests.helpers.decorators import create_db, instance
from tests.helpers.utils import add_product, retrieve_products, retrieve_product

logging.disable(logging.CRITICAL)


@create_db
def test_should_fetch_first_10_products_in_asc_order():
    EXPECTED_LENGTH = 10
    for i in range(1, 20):
        product = {'id': i, 'name': 'Some product', 'price': 1000 - 5*i}
        add_product(db, **product)
    with instance.application.app_context():
        response = instance.get('/products/')
        products = retrieve_products(response.data)
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
        response = instance.get('/products/kids/')
        products = retrieve_products(response.data)
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
        products = retrieve_products(response.data)
        assert len(products) == EXPECTED_LENGTH
        for i in range(10):
            assert products[i]['id'] == i + 1

        response = instance.get('/products/?page=2')
        products = retrieve_products(response.data)
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
        products = retrieve_products(response.data)
        assert len(products) == EXPECTED_LENGTH
        for i in range(10):
            assert products[i]['id'] == i + 1


@create_db
def test_fetch_product_by_valid_id():
    product = {'id': 42, 'name': 'Some product', 'price': 10.0}
    add_product(db, **product)
    with instance.application.app_context():
        response = instance.get('/products/42/')
        product = retrieve_product(response.data)
        assert product['id'] == 42
        assert product['name'] == 'Some product'
        assert float(product['price']) == 10.0


@create_db
def test_fetch_non_existent_product():
    product = {'id': 42, 'name': 'Some product', 'price': 10.0}
    add_product(db, **product)
    with instance.application.app_context():
        response = instance.get('/products/100500/')
        assert response.status == '400 BAD REQUEST'


@create_db
def test_fetch_product_with_non_valid_id():
    product = {'id': 42, 'name': 'Some product', 'price': 10.0}
    add_product(db, **product)
    with instance.application.app_context():
        response = instance.get('/products/GARBAGE/')
        assert response.status == '400 BAD REQUEST'


@create_db
def test_delete_product():
    product = {'id': 42, 'name': 'Some product', 'price': 10.0}
    add_product(db, **product)
    with instance.application.app_context():
        response = instance.delete('/product/42/')
        assert response.status == '200 OK'
        item = Product.query.get(42)
        assert item is None


@create_db
def test_create_product():
    data = {'name': 'Some product', 'price': 10.0, 'price_old': 5.0}
    with instance.application.app_context():
        response = instance.post('/product/', data=data)
        assert response.status == '302 FOUND'
        product = Product.query.filter_by(name='Some product').one()
        assert product is not None


@create_db
def test_update_product():
    product = {'id': 42, 'name': 'Some product', 'price': 10.0}
    add_product(db, **product)
    with instance.application.app_context():
        new_data = {'name': 'T-Shirt', 'price': 12.0}
        response = instance.put('/update-product/42/', data=new_data)
        assert response.status == '200 OK'
        product = Product.query.get(42)
        assert product.name == 'T-Shirt'
        assert product.price == 12.0


@create_db
def test_update_product_returns_status_400_on_exception():
    with instance.application.app_context():
        response = instance.put('/update-product/GARBAGE/', data=None)
        assert response.status == '400 BAD REQUEST'


@create_db
def test_delete_product_returns_400_on_exception():
    with instance.application.app_context():
        response = instance.delete('/product/42/')
        assert response.status == '400 BAD REQUEST'


@create_db
def test_manage_product_return_200_on_get_request():
    with instance.application.app_context():
        response = instance.get('/product/')
        assert response.status == '200 OK'


@create_db
def test_home_returns_200_on_get_request():
    with instance.application.app_context():
        response = instance.get('/')
        assert response.status == '200 OK'
