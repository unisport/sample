import unittest
from unittest import TestCase
from models import Products
from peewee import *
from app import app

test_db = SqliteDatabase(':memory:')

class MyTest(TestCase):
    def create_test_data(self):
        #create few names for products
        for i in range(5):
            Products.create(name='name-%s' % i)


@app.route('/products/kids/')
def kids_page():
    return Response()

if __name__ == '__main__':
    unittest.main()
