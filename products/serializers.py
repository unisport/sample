from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):

	is_customizable = serializers.CharField()
	delivery = serializers.CharField()
	kids = serializers.CharField()
	name = serializers.CharField()
	sizes = serializers.CharField()
	kid_adult = serializers.CharField()
	free_porto = serializers.CharField()
	image = serializers.URLField()
	package = serializers.CharField()
	price = serializers.DecimalField(
		max_digits=5, decimal_places=2,
		coerce_to_string=True, localize=True)
	url = serializers.URLField()
	price_old = serializers.DecimalField(
		max_digits=5, decimal_places=2,
		coerce_to_string=True, localize=True)
	currency = serializers.CharField()
	img_url = serializers.URLField()
	id = serializers.CharField(read_only=True)
	women = serializers.CharField()
	online = serializers.CharField()

	def create(self, validated_data):
		return Product.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.is_customizable = validated_data.get('is_customizable', 
			instance.is_customizable)
		instance.delivery = validated_data.get('delivery', instance.delivery)
		instance.kids = validated_data.get('kids', instance.kids)
		instance.name = validated_data.get('name', instance.name)
		instance.sizes = validated_data.get('sizes', instance.sizes)
		instance.kid_adult = validated_data.get('kid_adult', instance.kid_adult)
		instance.free_porto = validated_data.get('free_porto', instance.free_porto)
		instance.image = validated_data.get('image', instance.image)
		instance.package = validated_data.get('package', instance.package)
		instance.price = validated_data.get('price', instance.price)
		instance.url = validated_data.get('url', instance.url)
		instance.price_old = validated_data.get('price_old', instance.price_old)
		instance.currency = validated_data.get('currency', instance.currency)
		instance.img_url = validated_data.get('img_url', instance.img_url)
		instance.women = validated_data.get('women', instance.women)
		instance.online = validated_data.get('online', instance.online)
		return instance

