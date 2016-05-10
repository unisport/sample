from django.db import models
from django.core.urlresolvers import reverse
from djmoney.models.fields import MoneyField
from django.utils import timezone


class Size(models.Model):

    value = models.CharField(unique=True, max_length=50)

    class Meta:
        unique_together = ('id', 'value')

    def __unicode__(self):
        return self.value


class Product(models.Model):
    name = models.CharField(verbose_name='name', max_length=200)
    delivery = models.TextField(verbose_name='delivery', blank=True, max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    price_old = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    package = models.PositiveIntegerField(verbose_name='package', default=0)
    kids = models.PositiveIntegerField(verbose_name='kids', default=0)
    kid_adult = models.PositiveIntegerField(verbose_name='kid_adult', default=0)
    free_porto = models.PositiveIntegerField(verbose_name='free_porto', default=0)
    sizes = models.ManyToManyField(Size, related_query_name='sizes', default=[])
    url = models.URLField(verbose_name='url', blank=True)
    img_url = models.URLField(verbose_name='img_url', blank=True)
    image = models.URLField(verbose_name='image', blank=True)
    woman = models.PositiveSmallIntegerField(verbose_name='woman', default=0)
    online = models.PositiveSmallIntegerField(verbose_name='online', default=0)
    currency = models.CharField(max_length=12, blank=True)

    def get_absolute_url(self):
        return reverse('product', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
