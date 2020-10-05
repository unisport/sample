from products_service.models import Product
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('price')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductSerializer