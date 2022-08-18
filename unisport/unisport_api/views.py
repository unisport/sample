from rest_framework import viewsets

from unisport.unisport_api.serializers import (
    CurrencySerializer,
    ProductSerializer,
    StockSerializer,
)
from unisport.unisport_data.models import Currency, Product, Stock


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
