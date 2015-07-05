from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404, JsonResponse
from django.core.exceptions import ValidationError

from unisport.settings import PAGINATION_SIZE
from api.models import Product
from api.utils import convert_prices_from_danish_notation

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
            convert_prices_from_danish_notation(data)
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

    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404('Product not found')

        # check if format of the data is valid
        try:
            data = json.load(request)
        except ValueError as e:
            return JsonResponse({'status': 'Invalid format'}, status=400)

        convert_prices_from_danish_notation(data)
        # we want to only edit the provided fields
        for key, value in data.items():
            setattr(product, key, value)

        # validate the data
        # no errors - save it and return successful response
        # errors - return error response and indicate what is the problem
        try:
            product.full_clean()
            # only update newly edited fields
            product.save(update_fields=data.keys())
        except ValueError:
            return JsonResponse({'status': 'Invalid attribute'}, status=400)
        except ValidationError as e:
            return JsonResponse({'status': 'Validation errors', 'errors': e.message_dict}, status=400)

        return JsonResponse(product.to_dict())
