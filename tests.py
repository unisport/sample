"""
tests.py

This module is for testing, without using the unittest package.
There were some complications using the unittest package in regards
    to arrays of dicts, where it would falsely validate logically equal
    dicts as inequal. 

If any assertion error is thrown, it will print it out. Otherwise no output.
"""

import json
from requests import get

from money import Money
from utilities import paginate, parse_money, order_dict

def test_utilities():
    """
    Test the utilities.py module.
    """
    def test_paginate():
        """
        Tests the paginate() function.
        Most of the assertions are for testing any possible edge case using the paginate() function.
        """
        assert paginate([1, 2, 3, 4, 5, 6], 3) == [[1, 2, 3], [4, 5, 6]]
        assert paginate([1, 2, 3, 4, 5, 6, 7], 3) == [[1, 2, 3], [4, 5, 6], [7]]
        assert paginate([1, 2, 3, 4], 1) == [[1], [2], [3], [4]]
        assert paginate([1, 2, 3, 4, 5, 6], 6) == [[1, 2, 3, 4, 5, 6]]
        assert paginate([1, 2, 3, 4, 5, 6], 10) == [[1, 2, 3, 4, 5, 6]]
    
    def test_parse_money():
        """
        Tests the parse_money() function.
        Most of these tests are for testing any possible edge case with using Money()
        """
        assert parse_money("10.00", "USD") == Money("10", "USD")
        assert parse_money("10,00", "DKK") == Money("10", "DKK")
        assert parse_money("0,00", "DKK") == Money("0", "DKK")
        assert parse_money("0", "CAD") == Money("0", "CAD")
        assert parse_money("0.15", "CAD") == Money("0.15", "CAD")
        assert parse_money("0,15", "DKK") == Money("0.15", "DKK")
        assert parse_money("10.150,15", "DKK") == Money("10150.15", "DKK")
        # Money() throws, if its value-parameter contains thousands-separators.
        assert parse_money("10.150.000,15", "DKK") == Money("10150000.15", "DKK")
        # Also: its decimal-separator can only be a dot '.'
        assert parse_money("10.000.000,15", "DKK") == Money("10000000.15", "DKK")
        assert parse_money("10,000,000.15", "USD") == Money("10000000.15", "USD")

    def test_order_dict():
        """
        Tests the order_dict() function.
        These tests are for confirming that order_dict() as it should.
        """
        a = {
            "foo": "bar",
            "foz": "baz"
        }
        b = {
            "foz": "baz",
            "foo": "bar"
        }
        assert str(a) != str(b)
        assert a == b
        assert str(order_dict(a, a.keys())) == str(order_dict(b, a.keys()))

    test_paginate()
    test_parse_money()
    test_order_dict()

def test_web_service():
    """
    Test the webservice
    """
    def test_products():
        """
        Tests the /products endpoint.

        # As stated, the unittest package doesn't seem to properly work with arrays.
        # So no testing is done on whole arrays.
        # However, some general aspects are tested:
        #     known objects as the cheapest, the length of each page, error handling, etc.
        
        This way of running assertions actually work compared to the unittest package.
        """
        assert get("http://127.0.0.1:5000/products").json() == products[:10]
        assert get("http://127.0.0.1:5000/products?page=1").json() == products[:10]
        assert get(
            "http://127.0.0.1:5000/products?page=2").json() == products[10:20]
        assert get(
            "http://127.0.0.1:5000/products?page=3").json() == products[20:25]
        assert get("http://127.0.0.1:5000/products?page=4").status_code == 404


    def test_kids_products():
        kids_products = [
            {
                "is_customizable": "1",
                "delivery": "1-2 dage",
                "kids": "1",
                "name": "Fortuna Düsseldorf Hjemmebanetrøje 2016/17 Børn",
                "sizes": "YL/152 cm",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-7.unisport.dk/product/153344/7439bfeef274.jpg",
                "package": "0",
                "price": "137,00",
                "url": "https://www.unisport.dk/fodboldtroejer/fortuna-dusseldorf-hjemmebanetrje-201617-brn/153344/",
                "online": "1",
                "price_old": "549,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/153344_maxi_0.jpg",
                "id": "153344",
                "women": "0"
            },
            {
                "is_customizable": "1",
                "delivery": "1-2 dage",
                "kids": "1",
                "name": "Lyon Udebaneshorts 2017/18 Børn",
                "sizes": "128 cm, 140 cm, 152 cm, 164 cm, 176 cm",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-0.unisport.dk/product/161439/f0930fdcda2d.jpg",
                "package": "0",
                "price": "269,00",
                "url": "https://www.unisport.dk/fodboldtroejer/lyon-udebaneshorts-201718-brn/161439/",
                "online": "1",
                "price_old": "0,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/161439_maxi_0.jpg",
                "id": "161439",
                "women": "0"
            },
            {
                "is_customizable": "1",
                "delivery": "1-2 dage",
                "kids": "1",
                "name": "Lyon Hjemmebanesæt 2017/18 Mini-Kit Børn",
                "sizes": "92cm, 98cm, 104cm, 110cm, 116cm",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-1.unisport.dk/product/161437/1379174ec063.jpg",
                "package": "0",
                "price": "499,00",
                "url": "https://www.unisport.dk/fodboldtroejer/lyon-hjemmebanest-201718-mini-kit-brn/161437/",
                "online": "1",
                "price_old": "0,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/161437_maxi_0.jpg",
                "id": "161437",
                "women": "0"
            }
        ]
        assert get("http://127.0.0.1:5000/products/kids").json() == kids_products

    def test_product_by_id():
        a = {
            "currency": "DKK",
            "delivery": "1-2 dage",
            "free_porto": "0",
            "id": "153344",
            "image": "https://thumblr-7.unisport.dk/product/153344/7439bfeef274.jpg",
            "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/153344_maxi_0.jpg",
            "is_customizable": "1",
            "kid_adult": "0",
            "kids": "1",
            "name": "Fortuna Düsseldorf Hjemmebanetrøje 2016/17 Børn",
            "online": "1",
            "package": "0",
            "price": "137,00",
            "price_old": "549,00",
            "sizes": "YL/152 cm",
            "url": "https://www.unisport.dk/fodboldtroejer/fortuna-dusseldorf-hjemmebanetrje-201617-brn/153344/",
            "women": "0"
        }
        assert get("http://127.0.0.1:5000/products/153344").json() == a
        assert get("http://127.0.0.1:5000/products/2").status_code == 404

    test_products()
    test_kids_products()
    test_product_by_id()

def main(*tests):
    """
    Main function of the testing program.
    """
    for test in tests:
        print(f"Running {test.__name__}")
        test()

if __name__ == "__main__":
    with open("products.sorted.json", encoding="utf8") as sorted_products:
        products = json.load(sorted_products)
        main(test_utilities, test_web_service)
