import sqlite3
import urllib, json
from contextlib import closing

DATA_SOURCE = "https://www.unisport.dk/api/sample/"
DB_NAME = "products.db"
DB_SCHEMA = 'schema.sql'


#Database creation
connection = sqlite3.connect(DB_NAME) 

with sqlite3.connect(DB_NAME) as connection:
	with closing(connection.cursor()) as cursor:
		#Table creation
		with open(DB_SCHEMA) as schema:
			cursor.executescript(schema.read())
			
		#Initialize/populate table
		with closing(urllib.urlopen(DATA_SOURCE)) as response:
			products = json.loads(response.read())['products']
			#All keys have to exist
			cursor.executemany("INSERT INTO products (id, is_customizable, delivery, kids, name, sizes, kid_adult, free_porto, image, package, price, url, online, price_old, currency, img_url, women) VALUES (:id, :is_customizable, :delivery, :kids, :name, :sizes, :kid_adult, :free_porto, :image, :package, :price, :url, :online, :price_old, :currency, :img_url, :women)", products)
