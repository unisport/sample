from api.models import Product
from api.serializers import ProductSerializer
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


def products_view(request, page=None):
    page = 1 if page is None else page
    queryset = Product.objects.order_by('price').all()[(page-1)*10:10*page]
    serializer = ProductSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)


# Kids product view : shows all kids products
def kids_products_view(request, page=None):
    page = 1 if page is None else page
    queryset = Product.objects.all().filter(kids=True)[(page-1)*10:10*page]
    serializer = ProductSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)


# Product view : given an id return the product page
def single_product_view(request, id):
    try:
        queryset = Product.objects.get(id=id)
    except ObjectDoesNotExist:
        return JsonResponse({}, status=404)
    serializer = ProductSerializer(queryset)
    return JsonResponse(serializer.data, safe=False)
