from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()
    meta = models.JSONField(blank=True, null=True)

    class Meta:
        ordering = ['price']

    def __str__(self):
        return self.name
