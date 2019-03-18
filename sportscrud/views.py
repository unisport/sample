from rest_framework import viewsets, generics

from sportscrud.models import Product
from sportscrud.serializers import ProductSerializer


class ProductViewSet(
	generics.ListAPIView,
	generics.RetrieveAPIView,
	viewsets.GenericViewSet,
):
	""" We extend the list and retrieve view, and order by price."""

	queryset = Product.objects.all().order_by('price')
	serializer_class = ProductSerializer


class KidsViewSet(
	generics.ListAPIView,
	viewsets.GenericViewSet,
):
	""" Same as before, but we also filter by kids, and we do not extend the retrieve view,
		as there is no /kids/{id} endpoint.
	"""
	queryset = Product.objects.all().filter(kids=True).order_by('price')
	serializer_class = ProductSerializer
