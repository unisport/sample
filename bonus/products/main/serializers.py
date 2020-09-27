from rest_framework import serializers
from . import models

class ProductsSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Products
    fields = '__all__'