from django.db import models


class Product(models.Model):
    is_customizable = models.BooleanField()
    delivery = models.CharField(max_length=64)
    kids = models.BooleanField()
    name = models.CharField(max_length=64)
    relative_url = models.CharField(max_length=128)
    discount_percentage = models.PositiveIntegerField()
    kid_adult = models.BooleanField()
    free_porto = models.BooleanField()
    image = models.CharField(max_length=256)
    sizes = models.CharField(max_length=512)
    package = models.BooleanField()
    price = models.FloatField()
    discount_type = models.CharField(max_length=64)
    product_labels = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    online = models.BooleanField()
    price_old = models.FloatField()
    currency = models.CharField(max_length=32)
    img_url = models.CharField(max_length=256)
    women = models.BooleanField()

    class Meta:
        db_table = "unisport.products"
