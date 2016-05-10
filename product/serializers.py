from rest_framework import serializers
from .models import Product, Size


class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size


class ProductSerializer(serializers.ModelSerializer):

    sizes = SizeSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

