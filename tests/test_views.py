import unittest
from sportr import sportr


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        sportr.app.config['TESTING'] = True
        self.app = sportr.app.test_client()
        self.app.testing = True

    def test_products(self):
        r = self.app.get('/products/')
        self.assertEqual(r.status_code, 200)

    def test_products_sorting(self):
        """
        r = self.app.get('/products/1111/')
        self.assertEqual(r.status_code, 200)"""

    def test_pagination(self):
        """r = self.app.get('/products/1111/')
        self.assertEqual(r.status_code, 200)"""

    def test_products_kids(self):
        r = self.app.get('/products/kids/')
        self.assertEqual(r.status_code, 200)

    def test_products_kids_sorting(self):
        """
        r = self.app.get('/products/1111/')
        self.assertEqual(r.status_code, 200)"""

    def test_products_id(self):
        sportr.items.append('test')
        sportr.id_lookup['12345678'] = len(sportr.items) - 1
        r = self.app.get('/products/12345678/')
        self.assertEqual(r.status_code, 200)

    def test_products_id_invalid(self):
        """
        r = self.app.get('/products/NOT_A_VALID_ID/')
        self.assertEqual(r.status_code, 404)"""

    def test_404(self):
        r = self.app.get('/not/a/valid/path/')
        self.assertEqual(r.status_code, 404)
