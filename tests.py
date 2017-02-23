import unittest
from nose.tools import *
import logging
from paste.fixture import TestApp
import webservice
import json
from models import Product


def setup_func():
    pass


def teardown_func():
    pass


@with_setup(setup_func, teardown_func)
def test_hello_kitty():
    """
    This is just to ensure things are working
    """
    restApp = TestApp(webservice.app.wsgifunc(*[]))
    req = restApp.get("/hello_kitty")

    assert_equal("Hello, Kitty", req.body)


def test_products():
    """
    First item in the list has to be cheaper than the last item in the list
    """
    restApp = TestApp(webservice.app.wsgifunc(*[]))
    req = restApp.get('/products/')
    products = json.loads(req.body)

    assert products[0]['price'] < products[9]['price']


def test_product_kids():
    """
    https://www.unisport.dk/api/sample/ nothings for kids
    """
    pass


def test_product_pager():
    """
    Using ? in modern REST API's... comon
    """
    restApp = TestApp(webservice.app.wsgifunc(*[]))
    req = restApp.get('/products/1')
    product_list = json.loads(req.body)

    assert len(product_list) == 10


def test_product_id():
    """
    Pick a product and use the id as a URL
    parameter to get the product data
    """
    product = Product.get()

    restApp = TestApp(webservice.app.wsgifunc(*[]))
    req = restApp.get("/product/{0}/".format(product.product_id))
    product_data = json.loads(req.body)

    assert product.name == product_data['name']
