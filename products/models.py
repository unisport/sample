from django.core.validators import URLValidator
from django.db import models


class SourceSettings(models.Model):
    name = models.CharField(max_length=16, null=False, unique=True)
    value = models.BooleanField(default=False)


class Size(models.Model):
    size = models.CharField(max_length=16, unique=True)

    def __unicode__(self):
        return self.size


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=16)
    price_old = models.CharField(max_length=16)

    package = models.CharField(max_length=1, default="0")
    delivery = models.CharField(max_length=1, default="0")
    free_porto = models.CharField(max_length=16, default="False")
    kids = models.CharField(max_length=1, default="0")
    kid_adult = models.CharField(max_length=1, default="0")
    women = models.CharField(max_length=1, default="0")

    sizes = models.ManyToManyField(Size)

    url = models.URLField(null=False, validators=[URLValidator(), ])
    img_url = models.URLField(validators=[URLValidator(), ])

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('-name',)


