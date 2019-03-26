from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint for products
    """
    queryset = Product.objects.all().order_by('price')
    serializer_class = ProductSerializer

class KidsProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint for kids products
    """
    queryset = Product.objects.filter(kids=True).order_by('price')
    serializer_class = ProductSerializer
