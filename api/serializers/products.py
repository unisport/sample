from rest_framework import serializers
from api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model."""

    product_labels = serializers.ListField(
        child=serializers.DictField(allow_empty=True),
        allow_empty=True
    )

    class Meta:
        """Meta class."""

        model = Product
        fields = "__all__"
