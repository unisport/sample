from rest_framework import serializers

class ProductSerializer(serializers.Serializer):

	is_customizable = serializers.CharField()
	delivery = serializers.CharField()
	kids = serializers.CharField()
	name = serializers.CharField()
	sizes = serializers.CharField()
	kid_adult = serializers.CharField()
	free_porto = serializers.CharField()
	image = serializers.ImageField()
	package = serializers.CharField()
	price = serializers.CharField()
	url = serializers.URLField()
	price_old = serializers.CharField()
	currency = serializers.CharField()
	img_url = serializers.URLField()
	id = serializers.CharField()
	women = serializers.CharField()
