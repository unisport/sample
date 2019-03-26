from rest_framework import serializers
from .models import Product

"""
Define json that is returned from the views methods
"""
class ProductSerializer(serializers.HyperlinkedModelSerializer):
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
            'women'
        )
