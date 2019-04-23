# I have tried to keep my code for my views in this file, so I have a minimum of code in my html files.
import urllib.request
import json

from django.core.paginator import Paginator
from django.core.paginator import InvalidPage
from django.core.paginator import EmptyPage
from django.shortcuts import render
from challenge.models import Product


def index(request):  # View to a simple html file, with links to the other views
    return render(request, 'challenge/index.html')


def products(request):  # View for the 10 cheapest products, taken away any with zero in price. Zero priced items is in data2
    imported_data_db = import_from_db(10)
    return render(request, 'challenge/products.html', {'data': imported_data_db['data'], 'data2': imported_data_db['data2']})


def kids(request):  # View for the 10 cheapest products with 'kids' = True
    data = Product.objects.order_by('price') & Product.objects.filter(kids=True)        
    return render(request, 'challenge/kids.html', {'data': data})


def id(request, product_id):  # View for showing products by there ID in the URL
    data = Product.objects.filter(product_id=product_id)    
    return render(request, 'challenge/id.html', {'data':data})


def paging(request):  # View for paginating the products (10 each page)
    data = Product.objects.all()
    paginator = Paginator(data, 10)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)
    return render(request, 'challenge/paging.html', {'posts':posts})


def products_web(request):  # View for data directly from the web sample
    imported_data_web = import_from_web_sample()
    return render(request, 'challenge/products_web.html', {'data_web': imported_data_web})


def import_from_db(products_to_load):  # Function to get the number of products you want from the DB
    data = Product.objects.order_by('price')[:products_to_load]
    data2 = [x for x in data if x.price == 0]  # gathering the ones with price = 0, to exclude them
    diff = len(data) + len(data2)
    if diff > products_to_load:
        data = Product.objects.order_by('price')[:diff]
        data = [x for x in data if x.price != 0]
    return {'data': data, 'data2': data2}


def import_from_web_sample():  # Function to import data from the web sample
    url = urllib.request.urlopen("https://www.unisport.dk/api/sample/")
    import_data = json.loads(url.read())

    for x in import_data['products']:
        x['price'] = (x['price'])[:-2]
        x['price'] = int(x['price'])

    return import_data

