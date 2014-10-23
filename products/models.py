from django.core.validators import URLValidator
from django.db import models


class Size(models.Model):
    size = models.CharField(max_length=16)

    def __unicode__(self):
        return self.size


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    price_old = models.DecimalField(max_digits=16, decimal_places=2, default=0)

    package = models.IntegerField(default=0)
    delivery = models.IntegerField(default=0)
    free_porto = models.IntegerField(default=0)
    kids = models.IntegerField(default=0)
    kid_adult = models.IntegerField(default=0)
    woman = models.IntegerField(default=0)

    sizes = models.ManyToManyField(Size)

    url = models.URLField(null=False, validators=[URLValidator(), ])
    img_url = models.URLField(validators=[URLValidator(), ])

    def __unicode__(self):
        return self.name