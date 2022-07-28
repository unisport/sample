import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return HttpResponseRedirect('/products')


def products(request):
    """

    """
    # Data endpoint
    endpoint = 'https://www.unisport.dk/api/products/batch/?list=254169,238156,255396,238179,200777,226546,222413,246169,238180,238169,213591,250042,254170,222410,205989,250278,246181,253890,246679,257119,222652,250036,238692,257120,253156,226547,238099,223462,218285,222190,238422,226099,235148,222255,238950,205990,250279,244233,238819,257543,256607'

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
        response = requests.get(endpoint, timeout=10)

        # Convert response to json object
        json_data = response.json()

        # Products list
        full_products_list = json_data['products']

        # Sort products list based on price
        # Sort function
        def sortFunction(product):
            return product['prices']['max_price']

        full_products_list.sort(key=sortFunction)

        # Pagination variables (10 objects per page)
        full_products_list_length = len(full_products_list)
        last_object_number_on_current_page = page_number * 10
        first_object_number_on_current_page = last_object_number_on_current_page - 9
        has_prev_page = True if first_object_number_on_current_page > 1 else False
        has_next_page = True if last_object_number_on_current_page < full_products_list_length else False

        print(full_products_list)
        print(f'List length: {full_products_list_length}')
        print(f'First Object: {first_object_number_on_current_page}')
        print(f'Last Object: {last_object_number_on_current_page}')
        print(f'Has prev page: {has_prev_page}')
        print(f'Has next page: {has_next_page}')

    return HttpResponse(f'<h1>Products page</h1>')


def product_detail(request):
    return HttpResponse('<h1>Product detail</h1>')
