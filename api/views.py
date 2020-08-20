from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    """
    ProductViewSet that allows for:
    - Retrieving individual products
    - Listing all products
    - Creating products
    - Deleting products
    - Updating products
    - Listing only products for kids
    """

    queryset = Product.objects.all().order_by('price')
    serializer_class = ProductSerializer

    def get_queryset(self):
        # We use a different queryset when "kids" are requested
        if self.request.path == '/products/kids/':
            return self.queryset.filter(kids=True)
        return self.queryset
