# -*- coding: utf-8 -*-
from django.db import models
from unisample.api.product.utils import generate_item_permanent_id


class Product(models.Model):
    _permanent_id = models.CharField(max_length=32) # id used for customer support

    name = models.CharField(max_length=255)

    price     = models.DecimalField(max_digits=8, decimal_places=2)
    price_old = models.DecimalField(max_digits=8, decimal_places=2)

    kids      = models.IntegerField()
    kid_adult = models.IntegerField()
    women     = models.IntegerField()

    delivery   = models.CharField(max_length=64)     # For now just string
    free_porto = models.BooleanField(default=False)
    package    = models.IntegerField()

    sizes      = models.CharField(max_length=255)    # For now just string

    url = models.URLField()
    img_url = models.URLField()

    def save(self, *args, **kwargs):
        if not self._permanent_id:
            self._permanent_id = generate_item_permanent_id()
        return super(Product, self).save(*args, **kwargs)

    @property
    def permanent_id(self):
        return self._permanent_id

    def __unicode__(self):
        return self.name
