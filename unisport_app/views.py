import math
import requests
from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Product, Price, Stock, Currency

# Used in both products and product_detail views
base_url = 'https://www.unisport.dk/api/products/batch/?list='


def index(request):
    return HttpResponseRedirect('/products')


def products(request):
    # Product IDs:
    product_id_list = '254169,238156,255396,238179,200777,226546,222413,246169,238180,238169,213591,250042,254170,222410,205989,250278,246181,253890,246679,257119,222652,250036,238692,257120,253156,226547,238099,223462,218285,222190,238422,226099,235148,222255,238950,205990,250279,244233,238819,257543'
    # Data endpoint
    products_list_endpoint = f'{base_url}{product_id_list}'

    if request.method == 'GET':
        # Convert query string to python dictionary
        query_string = request.GET.dict()

        # Check if query string contains the key 'page'
        if not 'page' in query_string:
            # Default page
            page_number = 1
        else:
            # Page from query string - converted to integer
            page_number = int(query_string['page'])

        # Fetch endpoint
        response = requests.get(products_list_endpoint, timeout=10)

        # Convert response to json
        json_data = response.json()

        # Products list
        full_products_list = json_data['products']

        # Sort products list based on price
        # Sort function
        def sortFunction(product):
            return product['prices']['max_price']

        full_products_list.sort(key=sortFunction)

        # Pagination variables (10 objects per page)
        items_per_page = 10
        full_products_list_length = len(full_products_list)
        last_object_number_on_current_page = page_number * 10
        first_object_number_on_current_page = last_object_number_on_current_page - 9
        has_prev_page = True if page_number > 1 else False
        has_next_page = True if last_object_number_on_current_page < full_products_list_length else False
        products_list_current_page = full_products_list[first_object_number_on_current_page -
                                                        1:last_object_number_on_current_page]
        number_of_products_on_current_page = len(products_list_current_page)
        number_of_pages = math.ceil(full_products_list_length / items_per_page)

        context = {
            'products_list_current_page': products_list_current_page,
            'full_products_list_length': full_products_list_length,
            'first_object_number_on_current_page': first_object_number_on_current_page,
            'has_prev_page': has_prev_page,
            'has_next_page': has_next_page,
            'number_of_products_on_current_page': number_of_products_on_current_page,
            'prev_page_number': page_number - 1,
            'next_page_number': page_number + 1,
            'page_number': page_number,
            'number_of_pages': number_of_pages,
        }

    return render(request, 'unisport_app/products_list.html', context)


def product_detail(request, id):
    single_product_endpoint = f'{base_url}{id}'

    # Fetch data from endpoint
    response = requests.get(single_product_endpoint, timeout=10)

    # Convert response to json object
    json_data = response.json()

    # Product data
    product_data = json_data['products']

    # Check if there is a product with ID from URL
    if not product_data:
        context = {
            'error': f'Produktnummer {id} eksisterer ikke',
        }
        return render(request, 'unisport_app/error.html', context)

    product = product_data[0]
    price = product['prices']['max_price']

    context = {
        'product': product,
        'price': price,
    }

    return render(request, 'unisport_app/product_detail.html', context)


def products_from_db(request):
    # Update - based on discounted price:
    products_list = Product.objects.all().annotate(discount_price=F('price__max_price') -
                                                   F('price__max_price') * F('price__discount_percentage') / 100).order_by('discount_price')
    products_list_count = products_list.count()

    # First draft start:
    # Default ordering - by price - is set on Products model (class Meta)
    # products_list = Product.objects.all()
    # products_list_count = products_list.count()
    # First draft end:

    pagination = Paginator(products_list, 10)
    page = request.GET.get('page')
    product_list_on_current_page = pagination.get_page(page)
    context = {
        'product_list_on_current_page': product_list_on_current_page,
        'products_list_count': products_list_count,
    }

    return render(request, 'unisport_app/products_list_from_db.html', context)


def product_from_db_detail(request, id):
    try:
        product = Product.objects.get(unisport_id=id)
    except Product.DoesNotExist:
        context = {
            'error': f'Produktnummer {id} eksisterer ikke',
        }
        return render(request, 'unisport_app/error.html', context)

    # product = get_object_or_404(Product, unisport_id=id)
    context = {
        'product': product,
    }

    return render(request, 'unisport_app/product_detail_from_db.html', context)
