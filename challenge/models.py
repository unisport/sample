from django.db import models

'''
The data model for the project, which is also the DB layout.
This format is not optimised, as it is just for testing purposes.
I have commented out the data i do not use in this code_challenge.

If you change the format run following commands in the shell:
    py manage.py makemigrations
    py manage.py migrate
    
This will add the changes to the code. (ORM)
'''


class Product(models.Model):
    kids = models.BooleanField(null=True, blank=True)
    name = models.CharField(max_length=255, blank=True)
    # relative_url = models.CharField(max_length=255, blank=True)
    # discount_percentage = models.IntegerField(blank=True)
    kid_adult = models.BooleanField(null=True, blank=True)
    # free_porto = models.BooleanField()
    image = models.CharField(max_length=255, blank=True)
    # sizes = models.CharField(max_length=255)
    # package = models.BooleanField()
    price = models.FloatField(blank=True)
    # discount_type = models.CharField(max_length=255)
    # product_labels = models.CharField(max_length=255)
    # url = models.CharField(max_length=255)
    # online = models.BooleanField()
    price_old = models.FloatField(blank=True, default=0)
    currency = models.CharField(max_length=255, blank=True)
    img_url = models.CharField(max_length=255, blank=True)
    product_id = models.CharField(max_length=255, blank=True)
    # women = models.BooleanField()

    def __str__(self):
        return self.name
