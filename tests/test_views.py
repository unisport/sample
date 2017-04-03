import unittest
from sportr import sportr
from bs4 import BeautifulSoup


example_item = {
    "is_customizable": "1", "delivery": "1-2 dage", "kids": "0",
    "name": "St. Pauli Hjemmebaneshorts 2016/17", "sizes": "X-Large, XX-Large, 3XL",
    "kid_adult": "0", "free_porto": "0",
    "image": "https://d34aj0jffcqapo.cloudfront.net/product/151107/aedc2441abc7.jpg",
    "package": "0", "price": "209,00",
    "url": "https://www.unisport.dk/fodboldtroejer/st-pauli-hjemmebaneshorts-201617/151107/", "online": "1", "price_old": "299,00", "currency": "DKK", "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/151107_maxi_0.jpg",
    "id": "151107", "women": "0"
}


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        sportr.app.config['TESTING'] = True
        self.app = sportr.app.test_client()
        self.app.testing = True

    def _is_sorted(self, path):
        r = self.app.get(path)
        soup = BeautifulSoup(r.data, 'lxml')
        prices = soup.find_all(class_='price')
        new_prices = []
        prev = -float('inf')
        for price in prices:
            as_float = float(price.text.replace(',', '.'))
            self.assertGreaterEqual(as_float, prev)
            prev = as_float
            new_prices.append(as_float)
        return new_prices

    def test_products(self):
        r = self.app.get('/products/')
        self.assertEqual(r.status_code, 200)

    def test_products_sorting(self):
        prices = self._is_sorted('/products/')
        self.assertEqual(len(prices), 10)

    def test_pagination(self):
        for i in range(10):
            with sportr.app.test_request_context('/products/?page=%d' % i):
                    self.assertEqual(sportr.request.path, '/products/')
                    self.assertEqual(sportr.request.args.get('page', type=int), i)
        r = self.app.get('/products/?page=2')
        self.assertEqual(r.status_code, 200)

    def test_products_kids(self):
        r = self.app.get('/products/kids/')
        self.assertEqual(r.status_code, 200)

    def test_products_kids_sorting(self):
        self._is_sorted('/products/kids/')

    def test_products_id(self):
        sportr.items.append(example_item)
        sportr.id_lookup['12345678'] = len(sportr.items) - 1
        r = self.app.get('/products/12345678/')
        self.assertEqual(r.status_code, 200)

    def test_products_id_invalid(self):
        r = self.app.get('/products/NOT_A_VALID_ID/')
        self.assertEqual(r.status_code, 404)

    def test_404(self):
        r = self.app.get('/not/a/valid/path/')
        self.assertEqual(r.status_code, 404)
