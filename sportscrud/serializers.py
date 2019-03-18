
from rest_framework import serializers
from sportscrud.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	""" Serializer for the product model. I am unsure if i am supposed to return the exact same data types as the sample
		data, or if it is just the abstract information that has to stay the same. I am assuming the latter, and
		returning a float for the price and old_price. If it had to be a string, we would have to drop down to a base
		Serializer, and define each field manually, as seen below (although this breaks some of the current tests,
		as they expect the output to be a float). It should also be noted that it still would not be the exact same,
		as the localisation of the price string would change. So it would probably require a custom serializer field,
		unless it supports localization in the casting.
	"""

	class Meta:
		model = Product
		fields = (
			'is_customizable',
			'delivery',
			'kids',
			'name',
			'relative_url',
			'discount_percentage',
			'kid_adult',
			'free_porto',
			'image',
			'sizes',
			'package',
			'price',
			'discount_type',
			'product_labels',
			'url',
			'online',
			'price_old',
			'currency',
			'img_url',
			'women',
			'id',
		)


"""
class ProductSerializer(serializers.Serializer):

	is_customizable = serializers.BooleanField()

	delivery = serializers.CharField()

	kids = serializers.BooleanField()

	name = serializers.CharField()

	relative_url = serializers.CharField()

	discount_percentage = serializers.IntegerField()

	kid_adult = serializers.BooleanField()

	free_porto = serializers.BooleanField()

	image = serializers.CharField()

	sizes = serializers.CharField()

	package = serializers.BooleanField()

	# Convert back to string
	price = serializers.CharField()

	discount_type = serializers.CharField()

	product_labels = serializers.CharField()

	url = serializers.CharField()

	online = serializers.BooleanField()

	# Convert back to string
	price_old = serializers.CharField()

	currency = serializers.CharField()

	img_url = serializers.CharField()

	women = serializers.BooleanField()

	id = serializers.IntegerField()

	def update(self, instance, validated_data):
		# We only need to retrieve
		pass

	def create(self, validated_data):
		# We only need to retrieve
		pass
"""