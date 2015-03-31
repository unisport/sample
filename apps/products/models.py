# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals

from django.core.validators import URLValidator
from django.db import models


CHOICES = (
    ('0', 'No'),
    ('1', 'Yes'),
)


class Size(models.Model):
    size = models.CharField(max_length=40, unique=True)

    def __unicode__(self):
        return self.size


class Product(models.Model):
    name = models.CharField(max_length=512)

    kids = models.CharField(max_length=1, choices=CHOICES, default='0')
    women = models.CharField(max_length=1, choices=CHOICES, default='0')
    kid_adult = models.CharField(max_length=1, choices=CHOICES, default='0')

    package = models.CharField(max_length=1, choices=CHOICES, default='0')

    free_porto = models.BooleanField(default=False)
    delivery = models.CharField(max_length=64)

    sizes = models.ManyToManyField(Size)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_old = models.DecimalField(max_digits=10, decimal_places=2)

    url = models.CharField(max_length=512, validators=[URLValidator, ])
    img_url = models.CharField(max_length=512, validators=[URLValidator, ])

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ('price', )