"""REST operations for KAMS scans."""

from rest_framework import generics
from rest_framework.response import Response
from api.models import Product
from api.serializers import ProductSerializer
from django.shortcuts import get_object_or_404
import logging

logger = logging.getLogger('unisport')


class ProductViewDetail(
    generics.RetrieveUpdateDestroyAPIView
):
    """Product Viewset."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"

    def get(self, request, id):
        """Return single product from id."""
        product = get_object_or_404(self.queryset, pk=id)
        return Response(
            ProductSerializer(product).data
        )
