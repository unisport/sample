# -*- coding: utf-8 -*-
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
    Say Hello to the Kitty
    """
    restApp = TestApp(webservice.app.wsgifunc(*[]))
    req = restApp.get("/hello_kitty")

    assert_equal("Hello, Kitty", req.body)


def test_products():
    """
    Test first item in the list has to be cheaper
    than the last item in the list
    """
    restApp = TestApp(webservice.app.wsgifunc(*[]))
    req = restApp.get('/products/')
    products = json.loads(req.body)

    assert products[0]['price'] < products[9]['price']


def test_product_kids():
    """
    Test products for kids sorted by cheapest first
    """
    restApp = TestApp(webservice.app.wsgifunc(*[]))
    req = restApp.get('/products/kids/')
    products = json.loads(req.body)

    assert len(products) == 0


def test_product_pager():
    """
    Test paginating products is working
    Using ? in modern REST API's... comon
    """
    restApp = TestApp(webservice.app.wsgifunc(*[]))
    req = restApp.get('/products/?page=2')
    product_list = json.loads(req.body)

    assert len(product_list) == 10


def test_product_id():
    """
    Test that we get product data by product id
    when it's passed as a URL parameter
    """
    product = Product.get()

    restApp = TestApp(webservice.app.wsgifunc(*[]))
    req = restApp.get("/product/{0}/".format(product.product_id))
    product_data = json.loads(req.body)

    assert product.name == product_data['name']
