import unittest
import requests
import json

from unisport import load_data

class TestLoadMethods(unittest.TestCase):
  #Test that load returns a dict and that it has the product key
  def test_load(self):
    resp = load_data("https://www.unisport.dk/api/sample/")
    self.assertIsNotNone(resp)
    self.assertTrue('products' in resp)


#Test the various view functions
class TestResponses(unittest.TestCase):
  #Get data from the server (which must be running to complete these tests)
  def get_data(self, path):
    r = requests.get("http://localhost:5000/" + path)
    return json.loads(r.text)

  #Test the /products/ page
  def test_products_without_page(self):
    data = self.get_data("products/")
    self.assertTrue('products' in data)
    self.assertEquals(len(data['products']), 10)
    self.assertEquals(data['products'], sorted(data['products'], key=lambda k: k['price']))

  #Test that the products/?page function returns data that is different from /products/
  def test_products_with_page(self):
    page_1_data = self.get_data("products/")
    page_2_data = self.get_data("products/?page=2")
    self.assertTrue(('error' in page_2_data and len(page_2_data['products']) == 0)
                      or ('products' in page_2_data and len(page_2_data['products']) > 0))
    self.assertEquals(page_2_data['products'], sorted(page_2_data['products'], key=lambda k: k['price']))
    self.assertNotEqual(page_1_data, page_2_data)

  #Test that an out of bounds page returns error
  def test_products_with_out_of_bounds_page(self):
    data = self.get_data("products/?page=42")
    self.assertTrue('error' in data and data['error'] == 'No more products found')
    self.assertTrue('products' in data and len(data['products']) == 0)

  #Test that /products/kids/ returns a sorted list of products where kids=1 for all products
  def test_kids_products(self):
    data = self.get_data("products/kids/")
    self.assertTrue('products' in data)
    self.assertEquals(data['products'], filter(lambda k: k['kids'] == '1', data['products']))
    self.assertEquals(data['products'], sorted(data['products'], key=lambda k: k['price']))

  #Test that /products/<id> with a valid id returns a product, not an error
  def test_product_with_valid_id(self):
    data = self.get_data("products/1")
    self.assertFalse('error' in data)
    self.assertTrue('name' in data)    

  #Test that /products/<id> with an invalid id returns an error
  def test_product_with_invalid_id(self):
    data = self.get_data("products/2")
    self.assertTrue('error' in data and data['error'] == 'Product not found')


if __name__ == '__main__':
  unittest.main()