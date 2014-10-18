from django.core.urlresolvers import reverse
from django.db import models


class Product(models.Model):
    product_id = models.PositiveIntegerField()
    name = models.CharField(max_length=256)

    kids = models.IntegerField()
    kid_adult = models.IntegerField()
    women = models.IntegerField()
    package = models.IntegerField()

    free_porto = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    price_old = models.DecimalField(max_digits=12, decimal_places=2)
    delivery = models.CharField(max_length=64)

    url = models.CharField(max_length=512)
    img_url = models.CharField(max_length=512, null=True, blank=True)

    sizes = models.ManyToManyField('ProductSize')

    def get_absolute_url(self):
        return reverse('product_detail', args=(self.pk, ))

    def __unicode__(self):
        return self.name


class ProductSize(models.Model):
    name = models.CharField(max_length=64, db_index=True)

    def __unicode__(self):
        return self.name
