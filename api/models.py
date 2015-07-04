from django.db import models

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

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __unicode__(self):
        return self.name
