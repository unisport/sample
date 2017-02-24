# -*- coding: utf-8 -*-
from peewee import *
from playhouse.shortcuts import model_to_dict


def get_db():
    """
    Change this to suit your needs for DB
    """
    return SqliteDatabase('sample.db', threadlocals=True)


class Product(Model):
    """
    The product model has the fields that are
    required for this test, nothing else
    """
    name = CharField()
    for_kids = BooleanField()
    price = FloatField()
    product_id = IntegerField()

    class Meta:
        database = get_db()


def migrate():
    """
    Running this will drop the table and
    create it again
    """
    Product.drop_table(True)
    Product.create_table(True)
