from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True)
    sizes = models.CharField(max_length=350, default='', blank=True)
    delivery = models.CharField(max_length=150, default='', blank=True)
    price = models.DecimalField( max_digits=11, decimal_places=2, blank=True, default=0.00)
    price_old = models.DecimalField(max_digits=11, decimal_places=2, blank=True, default=0.00)
    url = models.URLField(default='', blank=True)
    img_url = models.URLField(default='', blank=True)
    kids = models.PositiveSmallIntegerField(default=0, blank=True)
    women = models.PositiveSmallIntegerField(default=0, blank=True)
    kid_adult = models.PositiveSmallIntegerField(default=0, blank=True)
    free_porto = models.PositiveSmallIntegerField(default=0, blank=True)
    package = models.PositiveSmallIntegerField(default=0, blank=True)


    def __str__(self):
        return self.name
