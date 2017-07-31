from django.db import models


# I've assumed all boolean fields as booleans as all values are 0 or 1
# and it makes sense to be this way.
class Product(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    is_customizable = models.BooleanField()
    delivery = models.CharField(max_length=255)
    kids = models.BooleanField()
    name = models.CharField(max_length=255)
    sizes = models.CharField(max_length=255, blank=True)
    kid_adult = models.BooleanField()
    free_porto = models.BooleanField()
    image = models.CharField(max_length=255)
    package = models.BooleanField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    url = models.CharField(max_length=255)
    online = models.BooleanField()
    price_old = models.DecimalField(max_digits=20, decimal_places=2)
    currency = models.CharField(max_length=10)
    img_url = models.CharField(max_length=255)
    women = models.BooleanField()

    class Meta:
        ordering = ('price',)
