import locale
import pymongo

locale.setlocale(locale.LC_ALL, 'danish_Denmark')
PRODUCTS_PER_PAGE = 10
connection_string = "mongodb://localhost:27017"
client = pymongo.MongoClient(connection_string)
db = client.product_database
collection = db.product_collection

products = db.products