import flask
import application


def test_should_fetch_first_10_products_in_asc_order():
    application.app.config['TESTING'] = True
    instance = application.app.test_client()
    EXPECTED_LENGTH = 10
    with instance.application.app_context():
        response = instance.get('/products')
        products = flask.json.loads(response.data)
        assert len(products) == EXPECTED_LENGTH
        assert all(products[i]['price'] <= products[i+1]['price'] for i in range(EXPECTED_LENGTH-1))


def test_returns_products_for_kids():
    application.app.config['TESTING'] = True
    instance = application.app.test_client()
    EXPECTED_LENGTH = 0
    with instance.application.app_context():
        response = instance.get('/products/kids')
        products = flask.json.loads(response.data)
        assert len(products) == EXPECTED_LENGTH
