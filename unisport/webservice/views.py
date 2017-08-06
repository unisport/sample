import json
from django.http.response import HttpResponse
import urllib.request
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from webservice.models import Product

URL = urllib.request.urlopen("https://www.unisport.dk/api/sample/")
data = json.loads(URL.read().decode())


def top_ten_cheapest(request):
    products = []

    for x in data['products']:
        products.append(
            Product(
                id=x['id'],
                name=x['name'],
                price=float(x['price'].replace(",", ".")),  # replacing , with dot because of float
                currency=x['currency'],
                kids=x['kids'],
            )
        )
    return render(request, 'product_listing.html', {'product': (sorted(products[0:9], key=lambda p: p.price, reverse=False))})


def kids(request):
    products = []

    for x in data['products']:
        if int(x['kids']) == 1:
            products.append(
                Product(
                    id=x['id'],
                    name=x['name'],
                    price=float(x['price'].replace(",", ".")), # replacing , with dot because of float
                    currency=x['currency'],
                    kids=int(x['kids']),
                    )
                )
    return render(request, 'product_listing.html', {'product': (sorted(products, key=lambda p: p.price, reverse=False))})


def choose_product(request, id):

    products = []

    for x in data['products']:
        if id == x['id']:
            products.append(
                Product(
                    id=x['id'],
                    name=x['name'],
                    price=float(x['price'].replace(",", ".")),  # replacing , with dot because of float
                    currency=x['currency'],
                    kids=x['kids']
                )
            )
            return render(request, 'product_listing.html', {'product': products})
        elif len(products) == 0:
            return HttpResponse('No such product')


def paginate(request):

    product_list = data['products']

    paginator = Paginator(product_list, 10)

    page = request.GET.get('page')
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(request, 'paginate_list.html', {'page': page})












