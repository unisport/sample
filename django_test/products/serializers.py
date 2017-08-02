from products.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'is_customizable',
            'delivery',
            'kids',
            'name',
            'sizes',
            'kid_adult',
            'free_porto',
            'image',
            'package',
            'price',
            'url',
            'online',
            'price_old',
            'currency',
            'img_url',
            'women'
        )
