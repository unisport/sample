import unittest, UnisportApp, json

class UnisportAppTest(unittest.TestCase):

    def setUp(self):
        self.app = UnisportApp.app.test_client()

    def test_products_for_page(self):
        products = json.loads(self.app.get('/products/?page=2').data)['products']

        self.assertEqual(len(products), 10)
        self.assertFalse(any(float(products[i]['price'].replace(',', '.')) > float(products[i+1]['price'].replace(',', '.')) for i in range(len(products)-1)))

        bad_page_response = self.app.get('/products/?page=-1')
        self.assertEqual(bad_page_response.status_code, 404)        

    def test_kids_products(self):
        products = json.loads(self.app.get('/products/kids/').data)['products']

        self.assertFalse(any(single_product['kids'] == '0' for single_product in products))

    def test_product_by_id(self):
        found_product = json.loads(self.app.get('/products/107/').data)

        self.assertEqual(found_product['id'], '107')

        not_found_response = self.app.get('/products/1295311/')
        self.assertEqual(not_found_response.status_code, 404)

if __name__ == '__main__':
    unittest.main()