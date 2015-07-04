from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator, InvalidPage
from unisport.settings import PAGINATION_SIZE
from django.http import Http404, JsonResponse

from api.models import Product
class ProductList(View):

    def get(self, request):
        page = request.GET.get('page', 1)
        products = Product.objects.order_by_price()

        # paginate products
        # if a page number is invalid return 404
        paginator = Paginator(products, PAGINATION_SIZE)
        try:
            products = paginator.page(page)
        except InvalidPage as e:
            raise Http404('Invalid page')

        # convert model instances to a list of dictionaries
        serialized_data = [product.to_dict() for product in products]

        return JsonResponse(serialized_data, safe=False)

class ProductKids(View):
    def get(self, request):
        kids_products = Product.objects.kids().order_by_price()
        serialized_data = [product.to_dict() for product in kids_products]
        return JsonResponse(serialized_data, safe=False)
