from peewee import *
from playhouse.shortcuts import model_to_dict


""" Extend this to use what ever database you like """
def get_db():
    return SqliteDatabase('sample.db', threadlocals=True)


""" TODO: describe why no basemodel was created """
class Product(Model):
    name = CharField()
    for_kids = BooleanField()
    price = FloatField()
    product_id = IntegerField()

    class Meta:
        database = get_db()


def migrate():
    Product.drop_table(True)
    Product.create_table(True)
