from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    kids = models.IntegerField()
    currency = models.CharField(max_length=100, )
    url = models.URLField()
    delivery = models.CharField(max_length=255, blank=True, null=True)
    package = models.IntegerField()
    kid_adult = models.IntegerField()
    free_porto = models.CharField(max_length=255)
    image = models.URLField()
    size = models.CharField(max_length=255, blank=True, null=True)
    online = models.IntegerField()
    price_old = models.DecimalField(max_digits=10, decimal_places=2)
    img_url = models.URLField()
    women = models.IntegerField()

    def __unicode__(self):
        return self.name
