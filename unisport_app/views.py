import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Price, Stock, Currency

# Used in both products and product_detail views
base_url = 'https://www.unisport.dk/api/products/batch/?list='


def index(request):
    return HttpResponseRedirect('/products')


def products(request):
    """

    """
    # Product IDs:
    product_id_list = '254169,238156,255396,238179,200777,226546,222413,246169,238180,238169,213591,250042,254170,222410,205989,250278,246181,253890,246679,257119,222652,250036,238692,257120,253156,226547,238099,223462,218285,222190,238422,226099,235148,222255,238950,205990,250279,244233,238819,257543,256607'
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
        products_list_current_page = full_products_list[first_object_number_on_current_page -
                                                        1:last_object_number_on_current_page]
        number_of_products_on_current_page = len(products_list_current_page)

        print(products_list_current_page)
        print(f'List length: {full_products_list_length}')
        print(f'First Object: {first_object_number_on_current_page}')
        print(f'Last Object: {last_object_number_on_current_page}')
        print(f'Has prev page: {has_prev_page}')
        print(f'Has next page: {has_next_page}')
        print(number_of_products_on_current_page)

        context = {
            'products_list_current_page': products_list_current_page,
            'full_products_list_length': full_products_list_length,
            'first_object_number_on_current_page': first_object_number_on_current_page,
            # 'last_object_number_on_current_page': last_object_number_on_current_page,
            'has_prev_page': has_prev_page,
            'has_next_page': has_next_page,
            'number_of_products_on_current_page': number_of_products_on_current_page,
            'prev_page_number': page_number - 1,
            'next_page_number': page_number + 1,
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

    ##################### TODO: REMOVE
    # Print product data
    # print(product_data)

    # Check if there is a product with ID from URL
    if not product_data:
        return HttpResponse('<h1>We could not find the product</h1>')

    product = product_data[0]
    # print(product)

    context = {
        'product': product,
    }

    # PRODUCT
    unisport_id = product['id']
    name = product['name']
    relative_url = product['relative_url']
    image = product['image']
    delivery = product['delivery']
    online = product['online']
    is_customizable = product['is_customizable']
    is_exclusive = product['is_exclusive']
    url = product['url']

    # print(f'unisport_id: {unisport_id}')
    # print(f'name: {name}')
    # print(f'relative_url: {relative_url}')
    # print(f'image: {image}')
    # print(f'delivery: {delivery}')
    # print(f'online: {online}')
    # print(f'is_customizable: {is_customizable}')
    # print(f'is_exclusive: {is_exclusive}')
    # print(f'url: {url}')

    # TODO: Put this inside a try / except
    product_instance = Product(unisport_id=unisport_id, name=name, relative_url=relative_url,
                               image=image, delivery=delivery, online=online, is_customizable=is_customizable, is_exclusive=is_exclusive, url=url)
    product_instance.save()
    print('Product Instance: ', product_instance)

    # for key, price in product['prices'].items():
    #print(f'{key} : {price}')
    # print(product['prices']['max_price'])

    max_price = product['prices']['max_price']
    min_price = product['prices']['min_price']
    currency = product['prices']['currency']
    discount_percentage = product['prices']['discount_percentage']
    recommended_retail_price = product['prices']['recommended_retail_price']

    # TODO: Put this inside a try / except
    price_instance = Price(product_id=Product.objects.get(unisport_id=unisport_id), max_price=max_price, min_price=min_price,
                           currency=Currency.objects.get(currency_code=currency), discount_percentage=discount_percentage, recommended_retail_price=recommended_retail_price)
    price_instance.save()
    print('Price Instance: ', price_instance)

    return render(request, 'unisport_app/product_detail.html', context)


product = {
    'id': '257120',
    'prices': {'max_price': 549, 'min_price': 549, 'currency': 'DKK', 'discount_percentage': 0, 'recommended_retail_price': 549},
    'name': 'Paris Saint-Germain Hjemmebanetrøje Qatar Airways 2022/23 Børn',
    'relative_url': '/fodboldtrojer/paris-saint-germain-hjemmebanetroje-qatar-airways-202223-born/257120/',
    'image': 'https://thumblr.uniid.it/product/257120/462a18fd5910.jpg',
    'delivery': '1-3 hverdage',
    'online': True,
    'labels': [{'color': '#ffffff', 'background_color': '#000000', 'name': 'Børn', 'active': True, 'id': 48, 'priority': 7}, {'color': '#ffffff', 'background_color': '#000000', 'name': 'Nyhed', 'active': True, 'id': 10, 'priority': 5}],
    'is_customizable': True,
    'is_exclusive': False,
    'stock': [{'price': 549, 'name': 'XS: 122-128 cm', 'order_by': 0, 'stock_info': '', 'is_marketplace': False, 'pk': 1855, 'name_short': '6-8 Years'}, {'price': 549, 'name': 'S: 128-137 cm', 'order_by': 1, 'stock_info': '', 'is_marketplace': False, 'pk': 1856, 'name_short': '8-10 Years'}, {'price': 549, 'name': 'M: 137-147 cm', 'order_by': 2, 'stock_info': '', 'is_marketplace': False, 'pk': 1857, 'name_short': '10-12 Years'}, {'price': 549, 'name': 'L: 147-158 cm', 'order_by': 3, 'stock_info': '', 'is_marketplace': False, 'pk': 1858, 'name_short': '12-14 Years'}, {'price': 549, 'name': 'XL: 158-170 cm', 'order_by': 4, 'stock_info': '', 'is_marketplace': False, 'pk': 1859, 'name_short': '14-16 Years'}],
    'currency': 'DKK',
    'url': 'https://www.unisport.dk/fodboldtrojer/paris-saint-germain-hjemmebanetroje-qatar-airways-202223-born/257120/',
    'attributes': {'color': ['Blue'], 'gender': ["Men's"], 'item_type': 'Football shirts', 'players': ['N/A'], 'league': 'N/A', 'teamsport': 'N/A', 'club_national': 'Clubs', 'print_type': 'N/A', 'team': 'Paris Saint Germain', 'shirt_season': '2022/23', 'pricepoint': 'Fan shirts', 'nationality': 'France', 'sleeve': 'Short sleeves', 'segment': 'License', 'kit': 'Home Kits', 'print_color': 'White', 'brand': 'Nike', 'sorting_shirts': 'N/A', 'age': ['Kids'], 'quarter': 'Carry Over'}
}
