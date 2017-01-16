import json

from annoying.decorators import render_to
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, get_object_or_404

import requests

from . import forms
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
    return {'product': get_object_or_404(models.Product, pk=pk)}

@render_to('products/form.html')
def add_product(request):

    if request.method == 'POST':
        form = forms.ProductForm(request.POST)

        if form.is_valid():
            instance = form.save()
            return redirect(instance.get_absolute_url())
    else:
        form = forms.ProductForm()

    return {'form': form}

@render_to('products/form.html')
def change_product(request, pk=None):

    instance = get_object_or_404(models.Product, pk=pk) if pk else None

    if request.method == 'POST':
        form = forms.ProductForm(request.POST, instance=instance)

        if form.is_valid():
            instance = form.save()
            return redirect(instance.get_absolute_url())
    elif pk:
        instance = get_object_or_404(models.Product, pk=pk)
        form = forms.ProductForm(instance=instance)
    else:
        form = forms.ProductForm()

    return {'form': form}

def delete_product(request, pk=None):

    instance = get_object_or_404(models.Product, pk=pk)
    instance.delete()

    messages.info(request, 'Product was successfully deleted')
    return redirect(reverse('product_list'))
