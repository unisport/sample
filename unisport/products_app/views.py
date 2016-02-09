from rest_framework import mixins
from rest_framework.decorators import list_route
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from . models import Products
from . serializers import ProductSerializer
from rest_framework.response import Response


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class ProductViewSet(viewsets.ModelViewSet, mixins.DestroyModelMixin):
    """View for products"""

    queryset = Products.objects.all().order_by('price')
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    @list_route(methods=['get'])
    def kids(self, request):
        prod_kids = Products.objects.all().filter(kids=1).order_by('price')
        serializer = self.get_serializer(prod_kids, many=True)
        return Response(serializer.data)
