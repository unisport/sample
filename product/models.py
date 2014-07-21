# coding=utf-8

from django.db import models


class Product(models.Model):
    """
    Product model

    Note: 
        from Unisport API, it seems all fields are not blank
        id is the primary key in this service while pid is the ID from Unisport
    """

    pid = models.IntegerField(unique=True)
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    price_old = models.DecimalField(max_digits=16, decimal_places=2)
    img_url = models.URLField()
    url = models.URLField()

    package = models.IntegerField()
    min_delivery_day = models.IntegerField(default=7)  # it never hurts to have high min date
    max_delivery_day = models.IntegerField(default=7)

    free_porto = models.BooleanField()
    kid_adult = models.IntegerField()
    kids = models.IntegerField(db_index=True)
    women = models.IntegerField()

    sizes = models.ManyToManyField('product.Size')

    def __unicode__(self):
        return u'id:{0} {1}'.format(self.pid, self.name)

    @property
    def delivery(self):
        return u'{0}-{1} dage'.format(self.min_delivery_day, self.max_delivery_day)

    def as_json(self):
        """
        Returns exactly the same json string as Unisport does for a product
        Note, the sequence of `sizes` cannot be guaranteed 
        """
        json = {}

        _exclude_fileds = ['size', 'id', 'pid', 'min_delivery_day', 'max_delivery_day']

        for field in self._meta.fields:
            if field.name not in _exclude_fileds:
                json[field.name] = unicode(getattr(self, field.name))

        json['id'] = self.pid
        json['delivery'] = self.delivery
        json['sizes'] = u','.join([s.name for s in self.sizes.all()])

        return json


class Size(models.Model):
    name = models.CharField(max_length=128)
