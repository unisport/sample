from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404, JsonResponse
from django.core.exceptions import ValidationError

from unisport.settings import PAGINATION_SIZE
from api.models import Product

import json

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

    def post(self, request):

        # check if format of the data is valid
        try:
            data = json.load(request)
        except ValueError as e:
            return JsonResponse({'status': 'Invalid format'}, status=400)

        # validate the data
        # no errors - save it and return successful response
        # errors - return error response and indicate what is the problem
        try:
            product = Product(**data)
            product.full_clean()
            product.save()
        except TypeError:
            return JsonResponse({'status': 'Invalid attribute'}, status=400)
        except ValidationError as e:
            return JsonResponse({'status': 'Validation errors', 'errors': e.message_dict}, status=400)

        return JsonResponse({'status': 'Created', 'product': product.to_dict()}, status=201)


class ProductKids(View):
    def get(self, request):
        kids_products = Product.objects.kids().order_by_price()
        serialized_data = [product.to_dict() for product in kids_products]
        return JsonResponse(serialized_data, safe=False)

class ProductDetail(View):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404('Product not found')

        return JsonResponse(product.to_dict())
