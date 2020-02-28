"""REST operations for KAMS scans."""

from rest_framework import generics
from api.models import Product
from api.serializers import ProductSerializer
import logging

logger = logging.getLogger('unisport')


class ProductViewAge(
    generics.ListAPIView
):
    """Product Viewset."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, age):
        """Return queryset based on gender."""
        products = self.queryset.filter(
            attribute_english__age__contains=age.capitalize()
        )
        page = self.paginate_queryset(products)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
