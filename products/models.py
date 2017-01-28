from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    price_old = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.CharField(max_length=3)
    sizes = models.TextField()
    delivery = models.CharField(
        max_length=8,
        choices=[
            ('1-2 dage', '1-2 dage'),
        ],
    )

    url = models.URLField()
    image = models.URLField()
    img_url = models.URLField()

    is_customizable = models.BooleanField(default=False)
    kids = models.BooleanField(default=False)
    kid_adult = models.BooleanField(default=False)
    women = models.BooleanField(default=True)
    package = models.BooleanField(default=False)
    free_porto = models.BooleanField(default=False)
    online = models.BooleanField(default=False)

    def __str__(self):
        return self.name
