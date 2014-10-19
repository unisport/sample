from django.core.urlresolvers import reverse
from django.core.validators import URLValidator
from django.db import models


class Product(models.Model):
    product_id = models.PositiveIntegerField()
    name = models.CharField(max_length=256)

    """
    It would be more user-friendly if the fields "kids", "kid_adult", "women", "package" were boolean.
    But there was nothing said about this in the task..
    """
    kids = models.IntegerField(default=0)
    kid_adult = models.IntegerField(default=0)
    women = models.IntegerField(default=0)
    package = models.IntegerField(default=0)

    free_porto = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    price_old = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    delivery = models.CharField(max_length=64)

    url = models.CharField(max_length=512, validators=[URLValidator(), ])
    img_url = models.CharField(max_length=512, null=True, blank=True, validators=[URLValidator(), ])

    sizes = models.ManyToManyField('ProductSize')

    def get_absolute_url(self):
        return reverse('product_detail', args=(self.pk, ))

    def __unicode__(self):
        return self.name


class ProductSize(models.Model):
    name = models.CharField(max_length=64, db_index=True)

    def __unicode__(self):
        return self.name
