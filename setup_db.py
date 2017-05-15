import sqlite3
import urllib
import json
from contextlib import closing
import locale

locale.setlocale(locale.LC_ALL, 'da_DK.UTF-8')
DATA_SOURCE = "https://www.unisport.dk/api/sample/"
DB_NAME = "products.db"
DB_SCHEMA = 'schema.sql'


# Database creation
connection = sqlite3.connect(DB_NAME)

with sqlite3.connect(DB_NAME) as connection:
    with closing(connection.cursor()) as cursor:
        # Table creation
        with open(DB_SCHEMA) as schema:
            cursor.executescript(schema.read())

        # Initialize/populate table
        with closing(urllib.urlopen(DATA_SOURCE)) as response:
            products = json.loads(response.read())['products']

            # Cast values before the insert
            for product in products:
                product['price'] = locale.atof(product['price'])
                product['price_old'] = locale.atof(product['price_old'])

            # All keys have to exist
            cursor.executemany(
                "INSERT OR IGNORE INTO products (id, is_customizable, delivery, kids, \
                    name, sizes, kid_adult, free_porto, image, package, \
                    price, url, online, price_old, currency, img_url, women) \
                    VALUES (:id, :is_customizable, :delivery, :kids, :name, \
                    :sizes, :kid_adult, :free_porto, :image, :package, \
                    :price, :url, :online, :price_old, :currency, :img_url, \
                    :women)",
                products)
