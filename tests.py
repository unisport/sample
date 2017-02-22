import unittest
from nose.tools import *
import logging
from paste.fixture import TestApp
import webservice


def setup_func():
    pass

def teardown_func():
    pass


@with_setup(setup_func, teardown_func)
def test_products():
    restApp = TestApp(webservice.app.wsgifunc(*[]))
    req = restApp.get("/products")

    assert_equal("Hello, Kitty", req.body)


def test_product_kids():
    pass


def test_product_page():
    pass


def test_product_id():
    pass
