# code library imports
import json

# Django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

# project imports
from .models import Product


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the webshop index.")


def product_list(request):
    header_text = 'Product listing'
    lead_text = 'This is the product lead text'

    products = Product.objects.all()
    paginator = Paginator(products, 20)
    page = request.GET.get('page', 1)
    product_range = paginator.page(page)

    for product in product_range:
        # returning product labels as a list
        if product.labels != '':
            product.labels = product.labels.split(",")

        # limiting text lenght of product name
        product.name = product.name[:60] + "..."

        # formatting price from øre to kr with 2 decimals
        product.price = "{:.2f}".format(product.price / 100)

    context = {
        'header_text': header_text,
        'lead_text': lead_text,
        'products': product_range
    }
    return render(request, 'webshop/product_list.html', context=context)


def product_list_men(request):
    header_text = 'Mænd'
    lead_text = 'Listen af vores produkter til mænd'

    products = Product.objects.filter(gender__icontains="men's").filter(
        age__icontains="adults")

    paginator = Paginator(products, 20)
    page = request.GET.get('page', 1)
    product_range = paginator.page(page)

    for product in product_range:
        # returning product labels as a list
        if product.labels != '':
            product.labels = product.labels.split(",")

        # limiting text lenght of product name
        product.name = product.name[:60] + "..."

        # formatting price from øre to kr with 2 decimals
        product.price = "{:.2f}".format(product.price / 100)

    context = {
        'header_text': header_text,
        'lead_text': lead_text,
        'products': product_range
    }
    return render(request, 'webshop/product_list.html', context=context)


def product_list_women(request):
    header_text = 'Kvinder'
    lead_text = 'Listen af vores produkter til kvinder'

    products = Product.objects.filter(gender__icontains="women").filter(
        age__icontains="adults")

    paginator = Paginator(products, 20)
    page = request.GET.get('page', 1)
    product_range = paginator.page(page)

    for product in product_range:
        # returning product labels as a list
        if product.labels != '':
            product.labels = product.labels.split(",")

        # limiting text lenght of product name
        product.name = product.name[:60] + "..."

        # formatting price from øre to kr with 2 decimals
        product.price = "{:.2f}".format(product.price / 100)

    context = {
        'header_text': header_text,
        'lead_text': lead_text,
        'products': product_range
    }
    return render(request, 'webshop/product_list.html', context=context)


def product_list_kids(request):
    header_text = 'Børn'
    lead_text = 'Listen af vores produkter til børn'

    products = Product.objects.filter(age__icontains="kids")

    paginator = Paginator(products, 20)
    page = request.GET.get('page', 1)
    product_range = paginator.page(page)

    for product in product_range:
        # returning product labels as a list
        if product.labels != '':
            product.labels = product.labels.split(",")

        # limiting text lenght of product name
        product.name = product.name[:60] + "..."

        # formatting price from øre to kr with 2 decimals
        product.price = "{:.2f}".format(product.price / 100)

    context = {
        'header_text': header_text,
        'lead_text': lead_text,
        'products': product_range
    }
    return render(request, 'webshop/product_list.html', context=context)


def brand_list_nike(request):
    header_text = 'Nike'
    lead_text = 'Listen af vores produkter fra Nike'

    products = Product.objects.filter(brand__iexact='Nike')
    paginator = Paginator(products, 20)
    page = request.GET.get('page', 1)
    product_range = paginator.page(page)

    for product in product_range:
        # returning product labels as a list
        if product.labels != '':
            product.labels = product.labels.split(",")

        # limiting text lenght of product name
        product.name = product.name[:60] + "..."

        # formatting price from øre to kr with 2 decimals
        product.price = "{:.2f}".format(product.price / 100)

    context = {
        'header_text': header_text,
        'lead_text': lead_text,
        'products': product_range
    }
    return render(request, 'webshop/product_list.html', context=context)


def brand_list_adidas(request):
    header_text = 'Adidas'
    lead_text = 'Listen af vores produkter fra Adidas'

    products = Product.objects.filter(brand__iexact='adidas')
    paginator = Paginator(products, 20)
    page = request.GET.get('page', 1)
    product_range = paginator.page(page)

    for product in product_range:
        # returning product labels as a list
        if product.labels != '':
            product.labels = product.labels.split(",")

        # limiting text lenght of product name
        product.name = product.name[:60] + "..."

        # formatting price from øre to kr with 2 decimals
        product.price = "{:.2f}".format(product.price / 100)

    context = {
        'header_text': header_text,
        'lead_text': lead_text,
        'products': product_range
    }
    return render(request, 'webshop/product_list.html', context=context)


def import_data(request):

    files = []
    files.append('webshop/products_all.json')
    files.append('webshop/products_kids.json')
    files.append('webshop/products_womens.json')

    result_msg = ''
    for file_name in files:
        with open(file_name, 'r') as file:
            data = json.load(file)

        for product in data['products']:
            p = Product()
            p.unisport_id = product['id']
            p.brand = product['attributes']['brand']
            p.name = product['name']
            p.image = product['image']
            p.url = product['url']
            p.price = product['price']
            p.currency = product['currency']
            p.discount = product['discount_percentage']
            p.delivery = product['delivery']
            p.labels = ','.join(
                [label['name'] for label in product['product_labels']])
            p.sizes = ','.join([size['name'] for size in product['stock']])
            p.age = ','.join(product['attributes']['age'])
            p.gender = ','.join(product['attributes']['gender'])
            p.save()

        result_msg += "{num} products imported to database from {file_name}<br>".format(
            num=len(data['products']), file_name=file_name)

    return HttpResponse(result_msg)
