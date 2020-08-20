from django.db import models


class Product(models.Model):
    """
    Product model with a fields equal to a subset of what products have from the external API
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    discount_percentage = models.IntegerField()
    image = models.URLField()
    kids = models.BooleanField()

    def price_dkk(self):
        """Return the product price in DKK"""

        return self.price / 100
