from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pyunisport.utils import CustomPagination
from rest_framework import generics
from rest_framework import permissions
from .models import Product
from .serializers import ProductSerializer

class ListProducts(generics.ListAPIView):
    """List all products from database. Data
    is paginated."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = CustomPagination

class CreateProduct(generics.CreateAPIView):
    """View to create product object. Permissions are
    restricted to only allow Admins to submit data."""

    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAdminUser,)

class UpdateProduct(generics.UpdateAPIView):
    """View to update a product object of id 'product_id'.
    Permissions are restricted to only allow Admins to 
    submit data."""

    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_object(self):
        obj = Product.objects.get(id=self.kwargs["product_id"])
        return obj

class GetProduct(generics.RetrieveAPIView):
    """View to return a single product object of id 'product_id'."""
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductSerializer

    def get_object(self):
        obj = Product.objects.get(id=self.kwargs["product_id"])
        return obj

class ListKidsProducts(generics.ListAPIView):
    """List all kids products from database. Data
    is paginated."""
    queryset = Product.objects.filter(kids="1")
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = CustomPagination
