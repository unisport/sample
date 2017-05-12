from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Product(models.Model):
    price = models.DecimalField(max_digits=7, decimal_places=2)
    kids = models.CharField(max_length=1)
    price_old = models.DecimalField(max_digits=7, decimal_places=2)
    name = models.CharField(max_length=500)
    is_customizable = models.CharField(max_length=1)
    delivery = models.CharField(max_length=30)
    size = models.CharField(max_length=150)
    kid_adult = models.CharField(max_length=1)
    free_porto = models.CharField(max_length=1)
    image = models.CharField(max_length=500)
    package = models.CharField(max_length=1)
    url = models.CharField(max_length=500)
    online = models.CharField(max_length=1)
    currency = models.CharField(max_length=3)
    img_url = models.CharField(max_length=500)
    women = models.CharField(max_length=1)

    # To create a new object of product
    def get_absolute_url(self):
        return reverse('product:detail', kwargs={'pk': self.pk})

    # Create an accessable list for printing the detail of a particular object
    # A Trade of between using more memory and shorter code.
    # This function can be called directly in Django html template
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Product._meta.fields]