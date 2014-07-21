# coding=utf-8

from django.db import models


class Product(models.Model):

    p_id = models.IntegerField()
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    price_old = models.DecimalField(max_digits=16, decimal_places=2)
    img_url = models.URLField()
    url = models.URLField()

    package = models.IntegerField()
    min_delivery_day = models.IntegerField()
    max_delivery_day = models.IntegerField()

    free_porto = models.BooleanField()
    kid_adult = models.IntegerField()
    kids = models.IntegerField()
    women = models.IntegerField()

    sizes = models.ManyToManyField('product.Size')


class Size(models.Model):
    name = models.CharField(max_length=128)
