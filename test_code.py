from paste.fixture import TestApp
from nose.tools import *
from webserver import app

class TestCode():
    def test_kids(self):
        middleware = []
        testApp = TestApp(app.wsgifunc(*middleware))
        r = testApp.get('/')
        assert_equal(r.status, 200)
        for product in kid_products:
            assert_equal(product['kids'], u'1')   