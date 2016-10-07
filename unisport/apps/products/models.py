from __future__ import unicode_literals
from django.db import models


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    package = models.CharField(max_length=10)
    women = models.CharField(max_length=10)
    free_porto = models.CharField(max_length=10)
    delivery = models.CharField(max_length=50)
    image = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    online = models.CharField(max_length=10)
    sizes = models.CharField(max_length=1000)
    price_old = models.DecimalField(max_digits=10, decimal_places=2)
    kid_adult = models.CharField(max_length=20)
    kids = models.CharField(max_length=10)
    img_url = models.URLField()
    name = models.CharField(max_length=100)
    currency = models.CharField(max_length=10)
    url = models.URLField()

    def __str__(self):
        return self.name
