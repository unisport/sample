import unittest
import json
from Product import Product
from ProductJsonEncoder import ProductJsonEncoder

class ProductJsonEncoderTests(unittest.TestCase):
       def testEncodeProduct(self):
            product = Product()
            product.name = "name"
            product.kids = 0
            product.price = 123.45
            product.sizes = "sizes"
            product.delivery = "delivery"
            product.url = "url"
            product.img_url = "img_url"
            
            output = json.dumps(product, cls=ProductJsonEncoder)
            self.assertEqual('{"kids": 0, "name": "name", "package": "", "kid_adult": 0, "free_porto": 0, "price": 123.45, "sizes": "sizes", "delivery": "delivery", "url": "url", "price_old": 0, "img_url": "img_url", "id": 0, "women": 0}', output)
            
if __name__ == '__main__':
    unittest.main()
