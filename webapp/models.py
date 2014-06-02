from django.db import models

# Create your models here.

class Product(models.Model):
    

	kids = models.IntegerField()
	name = models.CharField(max_length=200)
	sizes = models.CharField(max_length=200)
	kid_adult = models.IntegerField()
	free_porto = models.BooleanField(default=False)
	price = models.FloatField(max_length=200)
	package = models.IntegerField()
	url = models.CharField(max_length=200)
	price_old = models.FloatField(max_length=200)    
	img_url = models.CharField(max_length=200)
	productID = models.IntegerField()
	women = models.IntegerField()

	def __unicode__(self):
		return '%s' % (self.id)

