from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Item(models.Model):
    """
    Model for holding the products.
    """
    name = models.CharField("name",max_length=100)
    kids = models.BooleanField(name="kids")
    price_old = models.FloatField(name="price_old")
    price = models.FloatField(name="price")
    url = models.CharField(name="url",max_length=128)
    img_url = models.CharField(name="img_url",max_length=128)
    women = models.BooleanField(name="women")
    kid_adult = models.BooleanField("kid_adult")
    free_porto = models.BooleanField(name="free_porto")
    sizes = models.CharField(name="sizes",max_length=256)
    package = models.BooleanField(name="package")
    delivery = models.CharField("delivery",max_length=20)

    class Meta:
        ordering = ['price']

    def get_absolute_url(self):
        """
        Gets the item corresponding to the id.
        """
        return reverse('products.item', args=[self.id])

    def __unicode__(self):
        return u'%s' % self.name

    def __str__(self):
        return self.title
