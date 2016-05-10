from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Product
from .utils import price_handler
from rest_framework import status
from rest_framework.response import Response


'''
simple api to GET and POST json data to db
'''
class ProductListAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()

    def post(self, request, *args, **kwargs):

        try:
            request.data.update({
                'price_old': price_handler(request.data['price_old']),
                'price': price_handler(request.data['price']),
            })
        except KeyError:
            pass
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


'''
simple api to update, delete product
'''
class ProductEditAPIView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (AllowAny,)
