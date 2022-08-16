from django.http import JsonResponse
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


#Post and list all in same class because they are not id spefic 
class ApiProductListView(ListAPIView):
    queryset = Product.objects.all().order_by("prices__recommended_retail_price")
    serializer_class = ProductSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination

    def post(self, request):
        data = request.data
        serializer = ProductSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        response = Response()

        response.data = {
            'message': 'Product Created Successfully',
            'data': serializer.data
        }

        return response


class ApiProductView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    pagination_class = PageNumberPagination

    def get_product(self, id):

        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            return None
    
    def get(self, request, id):
        
        product = self.get_product(id)
        if not product:
            return Response(
                {"res": "Product with this id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        
        product = self.get_product(id)
        if not product:
            return Response(
                {"res": "Product with this id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = ProductSerializer(instance=product, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        
        product = self.get_product(id)
        if not product:
            return Response(
                {"res": "Product with this id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        product.delete()
        return Response(
            {"res": "Product deleted!"},
            status=status.HTTP_200_OK
        )


