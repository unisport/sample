from django.db import models


class Product(models.Model):
    fake_id = models.PositiveIntegerField(unique=True, null=False)
    name = models.CharField(max_length=255)
    sizes = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    price_old = models.DecimalField(max_digits=16, decimal_places=2)
    delivery = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)

    # I am assuming these fields are actually boolean.
    kids = models.BooleanField()
    kid_adult = models.BooleanField()
    women = models.BooleanField()
    package = models.BooleanField()
    free_porto = models.BooleanField()
