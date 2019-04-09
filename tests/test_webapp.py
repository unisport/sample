import pytest
from app import app


#Testing index endpoint
@pytest.mark.test_index
def test_index():

    """
    GIVEN a request is made
    WHEN when the connection is established
    THEN status 200 ok is returned
    """""

    with app.test_client() as c:
        r = c.get('/')

        assert r.status_code == 302


#Testing products endpoint
@pytest.mark.test_products
def test_products():

    """
    GIVEN a request is made
    WHEN when the connection is established
    THEN status 200 ok is returned
    """""

    with app.test_client() as c:
        r = c.get('/products')

        assert r.status_code == 200


@pytest.mark.test_errorhandler
def test_error_handler():

    """
    GIVEN a product with a non existing ID is called
    WHEN when the page tries to load
    THEN you are on the error 404 page (status_code 404)
    """""

    with app.test_client() as c:
        r = c.get('/products/id/9999')

        assert r.status_code == 404