from rest_framework import serializers
from api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model."""

    class Meta:
        """Meta class."""

        model = Product
        fields = "__all__"
