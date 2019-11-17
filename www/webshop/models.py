from django.db import models


# Create your models here.
class Product(models.Model):
    unisport_id = models.IntegerField(blank=True)
    brand = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    image = models.URLField(max_length=2000, blank=True)
    url = models.URLField(max_length=2000, blank=True)
    price = models.IntegerField(blank=True, default=0)
    price_old = models.IntegerField(blank=True, default=0)
    currency = models.CharField(max_length=10, blank=True)
    discount = models.IntegerField(blank=True)
    delivery = models.CharField(max_length=255, blank=True)
    labels = models.CharField(max_length=255, blank=True)
    age = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=255, blank=True)
    sizes = models.TextField(max_length=1000, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
