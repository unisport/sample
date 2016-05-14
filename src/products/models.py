from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=360, null=False, blank=False)
	image = models.ImageField(upload_to='products/', null=True, blank=True)
	currency = models.CharField(max_length=50)
	delivery = models.CharField(max_length=200)
	kids = models.IntegerField(null=True, blank=True, default=0)
	package = models.IntegerField(null=True, blank=True, default=0)
	kid_adult = models.IntegerField(null=True, blank=True, default=0)
	# we can use models.BooleanFields or CharField in such fields
	# but it depends wich information in the project we want to store in this fields
	price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
	price_old = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True )
	women = models.IntegerField(null=True, blank=True, default=0)

	def __unicode__(self):
		return self.name
	


class Size(models.Model):
	product_size = models.ForeignKey(Product)
	size = models.CharField(max_length=720, default='One Size')

	def __unicode__(self):
		return self.size