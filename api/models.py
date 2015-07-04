from django.db import models


class ProductQuerySet(models.query.QuerySet):
    def order_by_price(self):
        return self.order_by('price')

    def kids(self):
        return self.filter(kids=1)

class Product(models.Model):

    name = models.CharField(max_length=256, unique=True)
    sizes = models.CharField(max_length=256)
    delivery = models.CharField(max_length=128)

    kids = models.BooleanField(default=False)
    kid_adult = models.BooleanField(default=False)
    free_porto = models.BooleanField(default=False)
    package = models.BooleanField(default=False)
    women = models.BooleanField(default=False)

    price = models.DecimalField(max_digits=8, decimal_places=2)
    price_old = models.DecimalField(max_digits=8, decimal_places=2)

    url = models.URLField()
    img_url = models.URLField()

    objects = ProductQuerySet.as_manager()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __unicode__(self):
        return self.name

    # convert model instance to a dictionary
    # boolean fields are represented as '1' or '0'
    # decimal fields are converted back to danish notation - 1099.00 becomes 1.099,00
    # all values are strings
    def to_dict(self):
        d = {}
        for field in self._meta.fields:
            value = getattr(self, field.name)
            if isinstance(field, models.BooleanField):
                value = '1' if value else '0'
            elif isinstance(field, models.DecimalField):
                value = '{0:,}'.format(value).replace('.', '?').replace(',', '.').replace('?', ',')
            d[field.name] = value
        return d
