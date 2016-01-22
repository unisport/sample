# encoding: utf-8
import urllib2
import json
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import JsonResponse, Http404
from django.views.generic import TemplateView
from django.conf import settings

from .models import Product, Size


class LoadDataView(TemplateView):
    """
    View for load initial data to DB
    """
    @staticmethod
    def create_sizes(sizes):
        sizes_objects = []
        for size in sizes:
            size_obj, created = Size.objects.get_or_create(value=size)
            sizes_objects.append(size_obj)
        return sizes_objects

    def get(self, request, *args, **kwargs):
        if settings.DATA_SOURCE:
            response_products = urllib2.urlopen(settings.DATA_SOURCE)
            products_json = json.load(response_products)
            if 'products' in products_json:
                for product_json in products_json['products']:
                    sizes_list = product_json.pop('sizes').split(',')
                    size_objects_list = LoadDataView.create_sizes(sizes_list)
                    for key in ['price', 'price_old']:
                        # replace . group delimiter
                        price_value = product_json[key].replace('.', '')
                        # replace , delimeter for decimal converting
                        product_json[key] = price_value.replace(',', '.')
                    product, created = Product.objects.get_or_create(
                        **product_json
                    )
                    if not created:
                        product.sizes.clear()
                    product.sizes.add(*size_objects_list)
                    try:
                        product.save()
                    # if modified init object saving
                    except IntegrityError:
                        pass

                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False})
        else:
            return JsonResponse({'success': False})


class CheapestProductsView(TemplateView):
    """
    View for selection of cheapest products
    """
    def get(self, request, *args, **kwargs):
        # try to get current page
        try:
            page = int(request.GET.get('page', 1))
        except ValueError:
            page = 1

        products_query = Product.objects.order_by('price')[page*10-10:page*10]
        return JsonResponse(
            {'products': [product.get_json() for product in products_query]}
        )


class KidsCheapestProductsView(TemplateView):
    """
    View for selection of cheapest products for kids
    """
    def get(self, request, *args, **kwargs):
        products_query = Product.objects.filter(kids='1').order_by('price')
        return JsonResponse(
            {'products': [product.get_json() for product in products_query]}
        )


class ProductView(TemplateView):
    """
    Product detail view
    """
    def get(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(pk=int(kwargs.get('pk')))
        except ObjectDoesNotExist:
            raise Http404
        return JsonResponse(
            {'product': product.get_json()}
        )
