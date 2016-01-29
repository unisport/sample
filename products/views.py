from django.http import JsonResponse
from django.core.paginator import Paginator
from products.models import Product
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ObjectDoesNotExist

# Amount of products to show on one page
PRODUCTS_ON_ONE_PAGE = 10

# All products field excluding 'id'
FIELDS = ['name', 'sizes', 'delivery', 'price', 'price_old', 'url',
          'img_url', 'kids', 'women', 'kid_adult', 'free_porto', 'package']


def convert_for_json(products_data):
    """Converts product items (products_data) to list of dictionaries.
    All values are converted to string"""
    converted_products = []
    for product in products_data:
        td = {k: str(v)
              for (k, v) in product.__dict__.items()
              if not k.startswith('_')}
        converted_products.append(td)
    return converted_products


def products(request):
    """View for products"""
    products_data = Product.objects.all().order_by('price')
    paginator = Paginator(products_data, PRODUCTS_ON_ONE_PAGE)

    try:
        # page number is passed through page value in GET request
        page_number = int(request.GET['page'])

        # To avoid code break inform if requested page number bigger then number of pages
        if page_number > paginator.num_pages:
            return JsonResponse({'status': 'error', 'reason': 'Empty Page'})

    except MultiValueDictKeyError:
        # if page number was not presented first page must be returned
        page_number = 1

    current_page = paginator.page(page_number)
    first_product = current_page.start_index() - 1
    last_product = current_page.end_index()

    products_slice = products_data[first_product:last_product]
    products_for_json = convert_for_json(products_slice)
    return JsonResponse({'products': products_for_json})


def products_kids(request):
    """products for kids view"""
    kid_products = Product.objects.filter(kids=1).order_by('price')
    kid_products_for_json = convert_for_json(kid_products)
    return JsonResponse({'products': kid_products_for_json})


def product_id(request, prod_id):
    """View for individual product"""
    if request.method == 'GET':
        prod_id = int(prod_id)

        try:
            product = Product.objects.get(id=prod_id)
        except ObjectDoesNotExist:
            # if product does not exists return status 'error'
            return JsonResponse({'status': 'error', 'reason': 'ObjectDoesNotExist'})

        product_for_json = convert_for_json([product])
        return JsonResponse({'products': product_for_json})

    elif request.method == 'POST' and 'action' in request.POST:

        parameters_for_new_product = dict()

        if request.POST['action'] == 'delete':
            # print('delete', prod_id)
            try:
                prod = Product.objects.get(id=prod_id)
                prod.delete()
                return JsonResponse({'status': 'ok'})

            except ObjectDoesNotExist:
                return JsonResponse({'status': 'error', 'reason': 'ObjectDoesNotExist'})

        if request.POST['action'] == 'update':
            # print('update', prod_id)
            try:
                Product.objects.get(id=prod_id)

                parameters_for_new_product['id'] = prod_id
                for field in FIELDS:
                    parameters_for_new_product[field] = request.POST[field]

                prod = Product(**parameters_for_new_product)
                prod.save()
                product_for_json = convert_for_json([prod])
                return JsonResponse({'status': 'ok', 'products': product_for_json})

            except ObjectDoesNotExist:
                return JsonResponse({'status': 'error', 'reason': 'ObjectDoesNotExist'})

        if request.POST['action'] == 'add':
            try:
                # Check that the product exists
                Product.objects.get(id=int(prod_id))

                # If product exists return error
                return JsonResponse({'status': 'error', 'reason': 'Object with id={} exist'.format(prod_id)})

            except ObjectDoesNotExist:
                # Only if product doesn't exist it can be created
                parameters_for_new_product['id'] = prod_id
                for field in FIELDS:
                    parameters_for_new_product[field] = request.POST[field]

                prod = Product(**parameters_for_new_product)
                prod.save()
                product_for_json = convert_for_json([prod])
                return JsonResponse({'status':'ok', 'products': product_for_json})
