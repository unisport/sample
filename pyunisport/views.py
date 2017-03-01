from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .utils import CustomPagination
from models import UniposortEndPoint
from .serializers import ProductSerializer
from rest_framework import generics
from rest_framework import permissions

usE = UniposortEndPoint()

class ListProducts(generics.ListAPIView):
    queryset = usE.get_all_products()
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = CustomPagination

class GetProduct(generics.RetrieveAPIView):
	
	permission_classes = (permissions.AllowAny,)
	serializer_class = ProductSerializer

	def get_object(self):
		obj = usE.get_product(self.kwargs["product_id"])
		return obj

class ListKidsProducts(generics.ListAPIView):
    queryset = usE.get_all_kids_products()
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = CustomPagination