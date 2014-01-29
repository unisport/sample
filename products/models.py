# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import URLValidator

# Static delivery types (could be a model like sizes, so it's possible to add/edit/remove sizes)
DELIVERY_TYPES = (
    ("1-2 dage", "1-2 dage"),
    ("4-8 dage", "4-8 dage"),
    ("5-10 dage", "5-10 dage"),
    ("5-14 dage", "5-14 dage")
)


# Sizes for products is stored in DB, so it's possible to add more sizes
class ProductSize(models.Model):
    title = models.CharField(max_length=50, verbose_name=u"Størrelse/Tekst")

    def __unicode__(self):
        return unicode(self.title)


#Product class, for saving JSON data in DB, and making it possible to add/edit/remove products
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Produktnavn")
    sizes = models.ManyToManyField(ProductSize, related_name="products", blank=True)
    url = models.CharField(max_length=200, verbose_name="URL", validators=[URLValidator()])
    img_url = models.CharField(max_length=200, verbose_name="URL billede", validators=[URLValidator()])
    delivery = models.CharField(max_length=9, choices=DELIVERY_TYPES, verbose_name="Leveringstid")
    price = models.FloatField(verbose_name="Pris")
    price_old = models.FloatField(verbose_name="Pris (gammel)", blank=True, null=True)
    kids = models.BooleanField(default=False, verbose_name="Kids")
    kid_adult = models.BooleanField(default=False, verbose_name="Kid Adult")
    women = models.BooleanField(default=False, verbose_name="Women")
    free_porto = models.BooleanField(default=False, verbose_name="Gratis porto")
    from_json = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.name)

    def save(self, *args, **kwargs):
        try:
            this = Product.objects.get(id=self.id)
            if this.price != self.price:
                self.price_old = this.price
        except Product.DoesNotExist:
            pass
        super(Product, self).save(*args, **kwargs)