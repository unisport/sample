from django.db import models


class Product(models.Model):
	""" Model representing products in the system. I talk a little about the different data types, even though it is all
		sample data.
	"""

	is_customizable = models.BooleanField()

	delivery = models.CharField(max_length=64)

	kids = models.BooleanField()

	name = models.CharField(max_length=64)

	relative_url = models.CharField(max_length=128)

	# I assume there can never be a negative discount on a product. The django documentation however says that this
	# field only can contain zero for backwards compatibility reasons, so maybe this would be better of as something
	# else.
	discount_percentage = models.PositiveIntegerField()

	kid_adult = models.BooleanField()

	free_porto = models.BooleanField()

	image = models.CharField(max_length=256)

	# Assuming there is some finite amount of products can have (although there do seem to be a lot of different size
	# notations), this should probably be a list enum values, or something like that.
	sizes = models.CharField(max_length=512)

	package = models.BooleanField()

	# I don't know much about business practises, but float errors in prices seems like a mess. Since i do not think
	# more than 2 decimals precision is ever required, this could be an integer (and then divide with 100 to get actual
	# value). That would probably be best implemented as a custom field type. That seems beyond the scope of this task,
	# do I will just keep it as a float.
	price = models.FloatField()

	# This should probably also be an enum
	discount_type = models.CharField(max_length=64)

	# I am unsure what kind of data this is meant to represent, since all the sample items only have en empty list.
	# This really should be a list (many-to-many, table of labels, and join-table) though .
	product_labels = models.CharField(max_length=256)

	url = models.CharField(max_length=256)

	online = models.BooleanField()

	# Same as with price.
	price_old = models.FloatField()

	# Should probably also be an enum many-to-one
	currency = models.CharField(max_length=32)

	img_url = models.CharField(max_length=256)

	women = models.BooleanField()