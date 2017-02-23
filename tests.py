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
    restApp = TestApp(webservice.app.wsgifunc(*[]))
    req = restApp.get("/hello_kitty")

    assert_equal("Hello, Kitty", req.body)


def test_products():
    restApp = TestApp(webservice.app.wsgifunc(*[]))
    req = restApp.get('/products/')
    products = json.loads(req.body)

    assert products[0]['price'] < products[9]['price']


def test_product_kids():
    pass


def test_product_page():
    pass


def test_product_id():
    product = Product.get()

    restApp = TestApp(webservice.app.wsgifunc(*[]))
    req = restApp.get("/product/{0}/".format(product.product_id))
    product_data = json.loads(req.body)

    assert product.name == product_data['name']
