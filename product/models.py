# coding=utf-8

from django.db import models


class Product(models.Model):

    pid = models.IntegerField()
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    price_old = models.DecimalField(max_digits=16, decimal_places=2)
    img_url = models.URLField()
    url = models.URLField()

    package = models.IntegerField()
    min_delivery_day = models.IntegerField()
    max_delivery_day = models.IntegerField()

    free_porto = models.BooleanField()
    kid_adult = models.IntegerField()
    kids = models.IntegerField()
    women = models.IntegerField()

    sizes = models.ManyToManyField('product.Size')

    def __unicode__(self):
        return u'id:{0} {1}'.format(self.pid, self.name)

    def as_json(self):
        json = {}

        _exclude_fileds = ['size', 'id', 'pid', 'min_delivery_day', 'max_delivery_day']

        for field in self._meta.fields:
            if field.name not in _exclude_fileds:
                json[field.name] = unicode(getattr(self, field.name))

        json['id'] = self.pid
        json['delivery'] = u'{0}-{1} dage'.format(self.min_delivery_day, self.max_delivery_day)
        json['sizes'] = u','.join([s.name for s in self.sizes.all()])

        return json


class Size(models.Model):
    name = models.CharField(max_length=128)
