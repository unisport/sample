from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.order_by('price')
    serializer_class = ProductSerializer


class KidsList(generics.ListCreateAPIView):
    queryset = Product.objects.filter(kids=1).order_by('price')
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
