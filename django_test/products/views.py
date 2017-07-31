from django.shortcuts import get_object_or_404
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

PAGE_SIZE = 10


class ProductList(APIView):
    """
    List all products or create a new product.
    """

    def get(self, request):
        if request.query_params.get('page'):
            page = int(request.query_params.get('page'))
            if page >= 1:
                products = Product.objects.all()[(page-1)*PAGE_SIZE:page*PAGE_SIZE]
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            products = Product.objects.all()[0:PAGE_SIZE]
        if not products:
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KidsProductList(APIView):
    """
    List all products where attribute kids is true.
    """

    def get(self, request):
        products = Product.objects.filter(kids=True)

        if not products:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    """
    Retrieve, update or delete a product instance.
    """

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        if int(pk) != int(request.data['id']):
            return Response(
                "Product ID %s doesn't match to edit product's %s" % (
                    str(pk),
                    str(request.data['id'])
                ),
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            product = Product.objects.get(pk=int(request.data['id']))
        except Product.DoesNotExist:
                serializer = ProductSerializer(data=request.data)
                code = status.HTTP_201_CREATED
        else:
            serializer = ProductSerializer(product, data=request.data)
            code = status.HTTP_200_OK

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=code)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
