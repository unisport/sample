import time
from peewee import *

db = SqliteDatabase('sample.db')

# Define a model class which specifies our database 
class Products(Model):
    created_date = DateTimeField(default=time.strftime("%Y-%m-%d %H:%M:%S"))
    kids = CharField(null=True)
    name = CharField(null=True)
    sizes = CharField(null=True)
    kid_adult = CharField(null=True)
    free_porto = CharField(null=True)
    price = DecimalField(null=True)
    package = CharField(null=True)
    delivery = CharField(null=True)
    url = CharField(null=True)
    price_old = DecimalField(null=True)
    img_url = CharField(null=True)
    product_id = CharField(null=True)
    women = CharField(null=True)

    class Meta:
        database = db # This model uses the "sample.db" database.
