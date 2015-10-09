from django.db import models, connection

import urllib2
import json
import logging

logger = logging.getLogger('unisport_test.models')

CHOICES = (('0', False), ('1', True))

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    price_old = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    sizes = models.TextField(max_length=350, default='')
    kid_adult = models.CharField(max_length=1, default='0', choices=CHOICES)
    kids = models.CharField(max_length=1, default='0', choices=CHOICES)
    free_porto = models.CharField(max_length=1, default='0', choices=CHOICES)
    women = models.CharField(max_length=1, default='0', choices=CHOICES)
    package = models.CharField(max_length=1, default='0', choices=CHOICES)
    delivery = models.CharField(max_length=12, default='1-2 dage')
    img_url = models.URLField(max_length=100, default='')
    url = models.URLField(max_length=100, default='')

    @classmethod
    def reset_table(cls):
        """
        remove all objects from table and reset table index
        """
        curs = connection.cursor()
        cls.objects.all().delete()
        curs.execute("delete from sqlite_sequence where name='{}';".format(cls._meta.db_table))

    @classmethod
    def reload_data(cls):
        """
        reset table and fill it from url: https://www.unisport.dk/api/sample/
        """
        cls.reset_table()
        try:
            responce = urllib2.urlopen('https://www.unisport.dk/api/sample/').read()
            product_raw_list = json.loads(responce)['products']
            cls.objects.bulk_create([cls(
                id=product_raw['id'],
                name=product_raw['name'],
                price=float(product_raw['price'].replace('.', '').replace(',', '.')),
                price_old=float(product_raw['price_old'].replace('.', '').replace(',', '.')),
                sizes=product_raw['sizes'],
                kid_adult=product_raw['kid_adult'],
                kids=product_raw['kids'],
                free_porto=product_raw['free_porto'],
                women=product_raw['women'],
                package=product_raw['package'],
                delivery=product_raw['delivery'],
                img_url=product_raw['img_url'],
                url=product_raw['url'],
            ) for product_raw in product_raw_list])
        except urllib2.HTTPError as e:
            logger.error(e)
        except (KeyError, ValueError):
            logger.error('Wrong json data')

    def __str__(self):
        return "Product: {}".format(self.id)


