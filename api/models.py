from django.db import models
from django.contrib.postgres import fields as pg_fields

DEFAULT_CURRENCY = "DKK"


class Product(models.Model):
    """Product model."""

    id = models.PositiveIntegerField(unique=True, primary_key=True)
    is_customizable = models.BooleanField(default=False)
    relative_url = models.CharField(max_length=255, default="")
    price = models.PositiveIntegerField(default=0)
    product_main_image = models.URLField(max_length=255)
    attribute_english = pg_fields.JSONField(default=dict)
    discount_type = models.CharField(null=True, max_length=50)
    prices = pg_fields.JSONField(default=dict)
    currency = models.CharField(max_length=5, default=DEFAULT_CURRENCY)
    delivery = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    discount_percentage = models.PositiveIntegerField(default=0)
    url = models.URLField(max_length=255)
    product_labels = pg_fields.ArrayField(
        base_field=pg_fields.JSONField(default=dict),
        default=list
    )
    online = models.BooleanField(default=True)
    price_old = models.CharField(max_length=10)
    attributes = pg_fields.JSONField(default=dict)
    min_max_prices = pg_fields.JSONField(default=dict)
    image = models.URLField(max_length=255)
    stock = pg_fields.JSONField(default=dict)
