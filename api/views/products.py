"""REST operations for KAMS scans."""

from rest_framework import generics
from api.models import Product
from api.serializers import ProductSerializer
import logging

logger = logging.getLogger('unisport')


class ProductView(
    generics.ListCreateAPIView,
):
    """Product Viewset."""

    serializer_class = ProductSerializer

    def get_queryset(self):
        """Return defualt queryset."""
        return Product.objects.all().order_by("price")
