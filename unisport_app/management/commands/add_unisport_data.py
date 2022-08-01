import requests
import random
from django.core.management.base import BaseCommand
from unisport_app.models import Product, Stock, Price, Currency

base_url = 'https://www.unisport.dk/api/products/batch/?list='
product_list = '257543,238179,254169,238161,250662,250659,246677,238159,238169,255396,226546,213591,254170,250665,238321,205989,235067,242532,238318,223466,235054,217710,226698,246679,250042,242774,257119,257120,218285,198079,217769,253890,253288,238847,226547,225705,246169,238819,222410,222652'


class Command(BaseCommand):

    # def add_arguments(self, parser):
    #     parser.add_argument('product_list', nargs='?',
    #                         type=str, default='None')

    def handle(self, **options):
        print('Adding Unisport data...')
        product_id_list = '257543,238179,254169,238161'
        #product_id_list = '225705,246169,238819,222410,222652'
        products_list_endpoint = f'{base_url}{product_list}'

        # Fetch endpoint
        response = requests.get(products_list_endpoint, timeout=10)

        # Convert response to json
        json_data = response.json()

        # Products list
        full_products_list = json_data['products']

        for product in full_products_list:
            # Variables for creating Product object
            unisport_id = product['id']
            name = product['name']
            relative_url = product['relative_url']
            image = product['image']
            delivery = product['delivery']
            online = product['online']
            is_customizable = product['is_customizable']
            is_exclusive = product['is_exclusive']
            url = product['url']

            # Create Product if it does not exist
            product_obj, created = Product.objects.get_or_create(unisport_id=unisport_id, name=name, relative_url=relative_url,
                                                                 image=image, delivery=delivery, online=online, is_customizable=is_customizable, is_exclusive=is_exclusive, url=url)
            print('Product object: ', product_obj)
            print('Created: ', created)

            # Variables for creating Price object
            max_price = product['prices']['max_price']
            min_price = product['prices']['min_price']
            currency = product['prices']['currency']
            discount_percentage = product['prices']['discount_percentage']
            recommended_retail_price = product['prices']['recommended_retail_price']

            price_obj, created = Price.objects.update_or_create(product_id=product_obj, max_price=max_price, min_price=min_price,
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
                    stock_object = Stock(product_id=product_obj, size=name, stock_quantity=random.randint(
                        0, 50), is_marketplace=is_marketplace, name_short=name_short)
                    stock_object.save()
                    print('***** Stock object created', stock_object)
