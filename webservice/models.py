__author__ = 'azhukov'

from django.db import models
from django.core.validators import URLValidator

class Item(models.Model):

    """"
    We use BooleanField, DecimalField and UrlField instead of CharField
    so we don't have to worry about validations. Also, correct usage of data types
    improves database performance
    """
    kids = models.BooleanField(default=None)
    name = models.CharField(max_length=256)
    sizes = models.CharField(max_length=256)
    kid_adult = models.BooleanField(default=None)
    free_porto = models.BooleanField(default=None)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0) # DecimalField allows us to use the default ordering
    price_old = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    package = models.BooleanField(default=None)
    delivery = models.CharField(max_length=20, default=0)
    url = models.URLField(validators=[URLValidator()], null=True, blank=True)
    img_url = models.URLField(validators=[URLValidator()], null=True, blank=True)
    women = models.BooleanField(default=None)

    # we need to create a custom primary key field
    id = models.CharField(primary_key=True, max_length=8)

    class Meta:
        ordering = ['price']




