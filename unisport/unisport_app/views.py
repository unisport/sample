from django.http import JsonResponse
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class ApiProductListView(ListAPIView):
    queryset = Product.objects.all().order_by("prices__recommended_retail_price")
    serializer_class = ProductSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination

class ApiProductView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_product(self, id):

        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            return None
    
    def get(self, request, id):
        
        product = self.get_product(id)
        if not product:
            return JsonResponse(
                {"res": "Object with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
