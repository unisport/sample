from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """ProductSerializer that serializes all Product fields"""

    class Meta:
        model = Product
        fields = '__all__'
