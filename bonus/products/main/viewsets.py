from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers


# Create your views here.
class ProductsViewSet(ModelViewSet):
  queryset = models.Products.objects.all()
  serializer_class = serializers.ProductsSerializer
