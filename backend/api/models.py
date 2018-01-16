from django.db import models


class Product(models.Model):
    is_customizable = models.BooleanField()
    delivery = models.CharField(max_length=20)
    kids = models.BooleanField()
    name = models.TextField()
    package = models.BooleanField()
    kid_adult = models.BooleanField()
    free_porto = models.BooleanField()
    thumbnail = models.URLField()
    sizes = models.TextField()
    # Price represented in øre to avoid decimal errors
    price = models.PositiveIntegerField()
    discount_type = models.CharField(max_length=20)  # Covers all cases
    online = models.BooleanField()
    # Same goes for price_old
    price_old = models.PositiveIntegerField()
    # According to ISO 4217 all currencies have three letter abbreviations
    currency = models.CharField(max_length=3)
    img_url = models.URLField()
    id = models.PositiveIntegerField(primary_key=True)
    # women = models.BooleanField()  # Has been left out as it is always 0
    # url = models.URLField()  # Has been left out as it points to the real site

