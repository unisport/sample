from sample import app, db, Product, ProductForm
import unittest


class DefaultDataBase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.db = db

    def test_get_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_first_page_products(self):
        response = self.app.get('/products/')
        self.assertEqual(response.status_code, 200)
        assert b'class=products start="1"' in response.data
        assert b'Gavekort' in response.data
        assert b'Prev page' not in response.data
        assert b'href="/products/?page=2">Next page' in response.data

    def test_second_page_products(self):
        response = self.app.get('/products/?page=2')
        self.assertEqual(response.status_code, 200)
        assert b'class=products start="11"' in response.data
        assert b'<a href="/products/?page=1">Prev page</a>' in response.data
        assert b'href="/products/?page=3">Next page' in response.data

    def test_last_page_products(self):
        response = self.app.get('/products/?page=3')
        self.assertEqual(response.status_code, 200)
        assert b'class=products start="21"' in response.data
        assert b'<a href="/products/?page=2">Prev page</a>' in response.data
        assert b'Next page' not in response.data

    def test_broke_page_products(self):
        response = self.app.get('/products/?page=4', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert b'We have 25 products, so the last page 3. ' \
               b'You have been redirect' in response.data
        assert b'class=products start="21"' in response.data

    def test_negative_page_products(self):
        response = self.app.get('/products/?page=-1', follow_redirects=True)
        assert b'Bad request: page must be integer type and more that 0.' \
               in response.data
        assert b'class=products start="1"' in response.data

    def test_zero_page_products(self):
        response = self.app.get('/products/?page=0', follow_redirects=True)
        assert b'Bad request: page must be integer type and more that 0.' \
               in response.data
        assert b'class=products start="1"' in response.data

    def test_kids_products_empty(self):
        response = self.app.get('/products/kids/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert b'Unfortunately we do not have products for kids now.' \
               in response.data

    def test_products_by_id(self):
        response = self.app.get('/products/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert b'form action="/products/1" method=post' \
               in response.data

    def test_products_by_wrong_id(self):
        response = self.app.get('/products/999999', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert b'The product with id=999999 not found' \
               in response.data


class EditDataBase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.db = db
        some_product = Product.query.first()
        setattr(some_product, 'kids', 1)
        self.db.session.commit()

    def test_kids_products_exist(self):

        response = self.app.get('/products/kids/')
        self.assertEqual(response.status_code, 200)
        assert b'Price: 0.0 <a href="/products/1">Gavekort' in response.data

    def test_broke_page_products_for_kids(self):
        response = self.app.get('/products/kids/?page=2',
                                follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert b'We have 1 products for kids, so the last page 1. ' \
               b'You have been redirect' in response.data

    def test_negative_page_products_for_kids(self):
        response = self.app.get('/products/kids/?page=-1',
                                follow_redirects=True)
        assert b'Bad request: page must be integer type and more that 0' \
               in response.data

    def test_delete_products_by_id(self):
        if not Product.query.get(34761):
            assert 0
        response = self.app.post('/products/34761', data={'submit': 'Delete'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert b'The product with id=34761 has been deleted' in response.data
        if Product.query.get(34761) is not None:
            assert 0

    def test_edit_products_by_id(self):
        product = Product.query.first()
        self.assertEqual(product.currency, 'DKK')

        form = ProductForm(obj=product)
        data = {**form.data, 'submit': 'Update', 'currency': 'EUR'}
        response = self.app.post('/products/{}'.format(product.id),
                                 data=data, follow_redirects=True)
        self.assertEqual(Product.query.first().currency, 'EUR')
        assert b'has been updated' in response.data

    def test_wrong_edit_products_by_id(self):
        product = Product.query.first()
        form = ProductForm(obj=product)
        data = {**form.data, 'submit': 'Update', 'currency': 'abracadabra'}
        response = self.app.post('/products/{}'.format(product.id),
                                 data={**data}, follow_redirects=True)
        assert b'Not a valid choice' in response.data
        self.assertEqual(Product.query.first().currency, product.currency)

    def test_create_products_by(self):
        some_product = Product.query.first()
        form = ProductForm(obj=some_product)
        data = {**form.data, 'submit': 'Update', 'name': 'New product'}
        response = self.app.post('/create_product', data={**data},
                                 follow_redirects=True)
        assert b'The product has been added with new id' in response.data

    def test_create_with_mistake_products_by(self):
        some_product = Product.query.first()
        form = ProductForm(obj=some_product)
        data = {**form.data, 'submit': 'Update', 'price': 'Not valid price'}
        response = self.app.post('/create_product', data={**data},
                                 follow_redirects=True)
        assert b'Not a valid float value' in response.data


class EmptyDataBase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.db = db
        Product.query.delete()

    def test_empty_products(self):
        response = self.app.get('/products/', follow_redirects=True)
        assert b'Unfortunately we do not have products now.' in response.data


if __name__ == '__main__':
    unittest.main()
