# encoding: utf-8
import simplejson

from django.db import models


class Size(models.Model):
    """
    Model for product sizes
    """
    value = models.CharField(max_length=15)

    def __unicode__(self):
        return self.value


class Product(models.Model):
    """
    Model for product
    """
    name = models.CharField(max_length=255)
    url = models.URLField()
    kid_adult = models.CharField(max_length=1)
    kids = models.CharField(max_length=1)
    women = models.CharField(max_length=1)
    sizes = models.ManyToManyField(Size)
    free_porto = models.CharField(max_length=1)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    price_old = models.DecimalField(max_digits=20, decimal_places=2)
    package = models.CharField(max_length=1)
    delivery = models.CharField(max_length=20)
    img_url = models.URLField()

    def __unicode__(self):
        return self.name

    def get_json(self):
        """
        return instance json string
        """
        obj_fields = dict.fromkeys(
            [field.name for field in Product._meta.fields], '')
        for field in obj_fields.keys():
            obj_fields[field] = getattr(self, field)
        obj_fields['sizes'] = self.get_sizes()
        return simplejson.dumps(obj_fields, use_decimal=True)

    def get_sizes(self):
        """
        return instance sizes string
        """
        return ', '.join([size.value for size in self.sizes.all()])
