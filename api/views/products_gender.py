"""REST operations for KAMS scans."""

from rest_framework import viewsets, mixins
from api.models import Product
from api.serializers import ProductSerializer
import logging

logger = logging.getLogger('unisport')


class ProductGenderViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
):
    """Product Viewset."""

    serializer_class = ProductSerializer

    def get_queryset(self):
        """Return Default queryset."""
        age = self.kwargs['age']
        return Product.objects.filter(
            attribute_english__age__contains=age.capitalize()
        ).order_by('price')
