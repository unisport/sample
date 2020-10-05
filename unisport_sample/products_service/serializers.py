from rest_framework import serializers
from products_service.models import Product

class ProductSerializer(serializers.ModelSerializer):
        class Meta:
                model = Product
                fields = '__all__'