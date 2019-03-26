import requests as r
from products.models import Product

"""
Class that is called from 'addproducts' command to import products from http://www.unisport.dk/api/sample/
"""
class ProductImport(object):
    _api_base_url = "http://www.unisport.dk/api/sample/"

    # Class method converting string to float.
    @classmethod
    def _clean_float(cls, val: str) -> float:
        return float(val.replace('.', '').replace(',', '.'))

    # Class method responsible for createing the products in the database
    @classmethod
    def _import(cls, products):
        for product in products:
            p = Product(
                is_customizable=product['is_customizable'],
                delivery=product['delivery'],
                kids=product['kids'],
                name=product['name'],
                relative_url=product['relative_url'],
                discount_percentage=product['discount_percentage'],
                kid_adult=product['kid_adult'],
                free_porto=product['free_porto'],
                image=product['image'],
                sizes=product['sizes'],
                package=product['package'],
                price=cls._clean_float(product['price']),
                discount_type=product['discount_type'],
                product_labels=product['product_labels'],
                url=product['url'],
                online=product['online'],
                price_old=cls._clean_float(product['price_old']),
                currency=product['currency'],
                img_url=product['img_url'],
                id=product['id'],
                women=product['women'],
            )
            p.save()

    # Class method responsible for fetching the data from the api and start the creating method
    @classmethod
    def do_import(cls):
        json_result = r.get(cls._api_base_url)
        if not json_result.ok or not json_result.json():
            return

        # Product.objects.all().delete()
        cls._import(json_result.json()['products'])
