from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Product


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the webshop index.")


def product_list(request):
    header_text = 'Product listing'
    lead_text = 'This is the product lead text'
    products = Product.objects.all()

    for product in products:
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
        'products': products
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
