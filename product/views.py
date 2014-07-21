# coding=utf-8

import json

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import Product


def _json_response(data):
    return HttpResponse(json.dumps(data), content_type='application/json')

def products(request):
    """
    List the cheapest 10 products
    Paginator is allowed
    """
    page = request.GET.get('page', 1)

    try:
        page = int(page)
    except ValueError:
        page = 1

    ps = Product.objects.all().prefetch_related('sizes').order_by('price')

    # get current page
    p = Paginator(ps, settings.PRODUCTS_PER_PAGE)
    page = p.page(page)

    resp = {'cheapest': []}
    for obj in page.object_list:
        resp['cheapest'].append(obj.as_json())

    return _json_response(resp)


def single_product(request, id):
    product = get_object_or_404(Product, pid=id)
    return _json_response(product.as_json())


def kids(request):
    ps = Product.objects.filter(kids=1).prefetch_related('sizes').order_by('price')

    resp = {'cheapest': []}
    for p in ps:
        resp['cheapest'].append(p.as_json())

    return _json_response(resp)
