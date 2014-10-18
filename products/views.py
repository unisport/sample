import json

from annoying.decorators import render_to
from annoying.functions import get_object_or_None
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

import requests

from . import models

API = 'http://www.unisport.dk/api/sample/'

def import_products(request):
    """
    Simple import. Enough for sample project.
    In the real life should be asynchronous(celery.task or something..) with validation, logging, etc.
    """

    for model in (models.Product, models.ProductSize):
        model.objects.all().delete()

    products = json.loads(requests.get(API).content).get('latest', [])

    for product in products:
        size_names = [size.strip() for size in product.pop('sizes', '').split(',')]

        product['product_id'] = product.pop('id')

        for field in ('price', 'price_old'):
            product[field] = product.get(field, '0').replace(',', '.')

        instance = models.Product.objects.create(**product)
        instance.sizes.add(*[models.ProductSize.objects.get_or_create(name=size_name)[0] for size_name in size_names])

    messages.info(request, '%d products were saved in the DB' % len(products))
    return redirect(reverse('product_list'))

@render_to('products/list.html')
def product_list(request, **kwargs):
    """
    Keyword arguments define filtering and ordering rules
    Example: product_list(request, ordering=('name', ), kids=1) will return queryset for /products/kids/ page ordered by name
    Default ordering is ('price', ) - cheapest first
    """
    ordering = kwargs.pop('ordering', ('price', ))
    paginator = Paginator(models.Product.objects.filter(**kwargs).order_by(*ordering), 10)

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return {'products': products}

@render_to('products/detail.html')
def product_detail(request, pk):

    return {'product': get_object_or_None(models.Product, pk=pk)}
