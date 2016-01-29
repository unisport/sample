from django.db import models


class Product(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    sizes = models.CharField(max_length=200)
    delivery = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    price_old = models.DecimalField(max_digits=9, decimal_places=2, default=0)

    url = models.URLField()
    img_url = models.URLField()

    kids = models.PositiveSmallIntegerField(default=0)
    women = models.PositiveSmallIntegerField(default=0)
    kid_adult = models.PositiveSmallIntegerField(default=0)
    free_porto = models.PositiveSmallIntegerField(default=0)
    package = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name
