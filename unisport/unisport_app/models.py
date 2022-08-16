from django.db import models

#created jsonfields instead of creating seperate databases and using foreign keys
#because the data is still just as accessible 

class Product(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    prices = models.JSONField(default=dict)
    name = models.TextField()
    relative_url = models.TextField()
    image = models.URLField()
    delivery = models.TextField()
    online = models.BooleanField()
    labels = models.JSONField(default=dict, blank=True)
    is_customizable = models.BooleanField()
    is_exclusive = models.BooleanField()
    stock = models.JSONField(default=dict)
    currency = models.CharField(max_length=5)
    url = models.URLField()
    attributes = models.JSONField(default=dict)
