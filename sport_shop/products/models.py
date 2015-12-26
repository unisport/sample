from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    """
    Description: Products with name, price, size etc.
    """
    #TODO Optimize char model max lenghts
    #TODO Normalize (sizes, delivery, and prices in separate tables)
    delivery = models.CharField(max_length=200)
    free_porto = models.BooleanField()
    img_url = models.CharField(max_length=500)
    kid_adult = models.BooleanField()
    kids = models.BooleanField()
    name = models.CharField(max_length=500)
    package = models.BooleanField()
    price = models.FloatField()
    price_old = models.FloatField()
    sizes = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    women = models.BooleanField()
