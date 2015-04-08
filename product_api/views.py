from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, pagination
from product_api.models import Product
from product_api.serializers import ProductSerializer


class SrandardResultsSetPagination(pagination.PageNumberPagination):
        page_size = 10
        page_size_query_param = 'page_size'
        max_page_size = 100


class ProductList(generics.ListAPIView):
    """
    List products.

    Return the first 10 products ordered with the cheapest first.
    Allow page number pagination.
    """
    queryset = Product.objects.order_by('price')
    serializer_class = ProductSerializer
    pagination_class = SrandardResultsSetPagination


@api_view(['GET'])
def product_kids(request):
    """
    List all products for kids.

    Return the products where kids=1 ordered with the cheapest first.
    """
    if request.method == 'GET':
        products = Product.objects.filter(kids__exact='1').order_by('price')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def product_id(request, product_id):
    """
    Return specific product.

    Return the product by id.
    """
    if request.method == 'GET':
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
