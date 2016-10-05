import unittest
from paste.fixture import TestApp

from core import app


class TestViews(unittest.TestCase):
    def setUp(self):
        self.testApp = TestApp(app.wsgifunc())

    def test_plist(self):
        r = self.testApp.get('/products/')
        self.assertEqual(r.status, 200)

    def test_pkids(self):
        r = self.testApp.get('/products/kids/')
        self.assertEqual(r.status, 200)

    def test_pdetail(self):
        r = self.testApp.get('/products/1/')
        self.assertEqual(r.status, 200)
        self.assertIn("u'id': u'1'", r.body)


suite = unittest.TestLoader().loadTestsFromTestCase(TestViews)
unittest.TextTestRunner(verbosity=2).run(suite)
