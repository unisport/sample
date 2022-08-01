import requests
import random
from django.test import TestCase
from django.db import IntegrityError
from .models import Product, Stock, Price, Currency


class UnisportTestCase(TestCase):

    def setUp(self):
        # Add Currencies:
        currency_dkk_obj = Currency.objects.create(currency_code='DKK')
        currency_eur_obj = Currency.objects.create(currency_code='EUR')
        currency_nok_obj = Currency.objects.create(currency_code='NOK')
        currency_sek_obj = Currency.objects.create(currency_code='SEK')

        # Add test data to db
        base_url = 'https://www.unisport.dk/api/products/batch/?list='
        product_list = '257543,238179,254169,238161,250662,250659,246677,238159,238169,255396,226546,213591,254170,250665,238321,205989,235067,242532,238318,223466,235054,217710'
        test_data_url = f'{base_url}{product_list}'

        # Fetch endpoint
        response = requests.get(test_data_url, timeout=10)

        # Convert response to json
        json_data = response.json()

        # Products list
        full_products_list = json_data['products']

        for product in full_products_list:
            unisport_id = product['id']
            name = product['name']
            relative_url = product['relative_url']
            image = product['image']
            delivery = product['delivery']
            online = product['online']
            is_customizable = product['is_customizable']
            is_exclusive = product['is_exclusive']
            url = product['url']
            product_obj = Product.objects.create(unisport_id=unisport_id, name=name, relative_url=relative_url,
                                                 image=image, delivery=delivery, online=online, is_customizable=is_customizable, is_exclusive=is_exclusive, url=url)

            max_price = product['prices']['max_price']
            min_price = product['prices']['min_price']
            currency = product['prices']['currency']
            discount_percentage = product['prices']['discount_percentage']
            recommended_retail_price = product['prices']['recommended_retail_price']

            price_obj = Price.objects.create(product_id=product_obj, max_price=max_price, min_price=min_price,
                                             currency=Currency.objects.get(currency_code=currency), discount_percentage=discount_percentage, recommended_retail_price=recommended_retail_price)

            # Save Stock data to database
            for item_in_stock in product['stock']:
                name = item_in_stock['name']
                is_marketplace = item_in_stock['is_marketplace']
                name_short = item_in_stock['name_short']

                try:
                    stock_object = Stock.objects.get(
                        product_id=product_obj, size=name)
                except Stock.DoesNotExist:
                    stock_object = Stock.objects.create(product_id=product_obj, size=name, stock_quantity=random.randint(
                        0, 50), is_marketplace=is_marketplace, name_short=name_short)

    def test_default_order(self):
        """
            Test default ordering of Product objects - by price (low to high).
        """
        full_products_list = Product.objects.all()
        for index, product in enumerate(full_products_list):
            if index == 0:
                continue
            else:
                assert full_products_list[index -
                                          1].price_dkk <= product.price_dkk

    def test_stock_model_unique_constraint(self):
        """
            Test unique constraint on Stock model. Make sure that product_id and size togehter are unique
        """
        first_product_object = Product.objects.all().first()
        print('** First product object: ', first_product_object)
        stock_obj_one = Stock.objects.create(
            product_id=first_product_object, size='Small', stock_quantity=5, is_marketplace=True, name_short='S')
        self.assertRaises(IntegrityError, Stock.objects.create, product_id=first_product_object,
                          size='Small', stock_quantity=20, is_marketplace=False, name_short='S')
