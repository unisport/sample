#coding: utf-8
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from unisport import settings
from unisport.product import models


def get_products(request):
    products = models.Product.objects.all().order_by('price')
    paginator = Paginator(products, settings.ELEMENTS_ON_PAGE)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        products = paginator.page(1)
    endpoint = reverse('products:get_products')
    products_payload = list(products.object_list.values())
    payload = dict(endpoint=endpoint, products=products_payload)

    return JsonResponse(payload)


def get_kids_product(request):
    products = models.Product.objects.filter(kids=1).order_by('price')
    endpoint = reverse('products:get_kids_product')
    products = list(products.values())
    payload = dict(endpoint=endpoint, products=products)
    return JsonResponse(payload)


def get_product_by_id(request, product_id):
    product = get_object_or_404(models.Product, pk=product_id)
    endpoint = reverse('products:get_product_by_id', kwargs={'product_id': product_id})
    product = model_to_dict(product)
    payload = dict(endpoint=endpoint, product=product)
    return JsonResponse(payload)

