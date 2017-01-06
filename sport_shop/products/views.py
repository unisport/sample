import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import HttpResponseForbidden
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Product


@require_http_methods("GET")
def listing_products(request, product_filter=None):
    """Lists all products sorted by price (ascending).

    Args: request (GET)
          product_filter (basestring): Filtering on the given attribute
            (must be boolean type) will be applied when getting
            list of products.
    Request parameters:
        page (int): Page number (limited amount of products on each page)
            default is 1.
        products_per_page (int): Number of products to show on page
            default is 10.
    Returns:
        HTTP response: List of products and page information is included in
            context when page is rendered. Rendered page has page indicator
            and navigation buttons to prev/next page if they exist.
            Page is validated and set to 1 if invalid.
    """
    products = None
    if product_filter:
        q_filter = {}
        q_filter[product_filter] = True
        products = Product.objects.filter(**q_filter).order_by('price').all()
    else:
        # All products ordered by price
        products = Product.objects.order_by('price').all()
    # Default pagination is 10 products per page
    products_per_page = request.GET.get('products_per_page', 10)
    paginator = Paginator(products, products_per_page)
    template = loader.get_template('products/listing_products.html')
    page = request.GET.get('page', 1)
    try:
        products_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = 1
        products_page = paginator.page(page)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page = paginator.num_pages
        products_page = paginator.page(page)
    try:
        prev_page = products_page.previous_page_number()
    except EmptyPage:
        prev_page = None
    try:
        next_page = products_page.next_page_number()
    except EmptyPage:
        next_page = None
    context = {
        'products': products_page,
        'pages_info': {
            'current': page,
            'count': paginator.num_pages,
            'previous': prev_page,
            'next': next_page,
        }
    }
    return HttpResponse(template.render(context, request))


@require_http_methods("GET")
def detail_product(request, product_id):
    """Detail view of single product.

    Args:
        request (GET)
        product_id (int): Product id is expected as suffix in URL.

    Returns:
        HTTP response: Product id is validated, if invalid, rendered page
            indicates that product is no longer available. A valid product id
            is used to get product object, which is included in context when
            rendering detailed product page.
    """
    try:
        product = Product.objects.get(id=product_id)
    except ObjectDoesNotExist:
        template = loader.get_template('products/product_not_exist.html')
        return HttpResponse(template.render(request))
    context = {'product': product}
    template = loader.get_template('products/detail_product.html')
    return HttpResponse(template.render(context, request))


@csrf_exempt
@require_http_methods("POST")
def create_product(request):
    """End point for creating new product.

    Args:
        request (POST)

    Request content: Expected content is a api token and a product object.
        in JSON type.

    Returns:
        HTTP Response: End point requires authentication, if successful,
            product object is validated and saved.

            Forbidden (403): If not authenticated.
            Bad Request (400): If product object can't be validated.

            Response with product id as JSON type is returned if successful.
    """
    # Dummy authentication
    request_data = json.loads(request.body)
    if request_data.get('api_token') != 'token':
        return HttpResponseForbidden()
    new_product = request_data.get('product')
    product = Product(**new_product)
    try:
        product.save()
    except AttributeError:
        return HttpResponseBadRequest()
    response_data = {'product_id': product.id}
    return HttpResponse(json.dumps(response_data),
                        content_type="application/json")


@csrf_exempt
@require_http_methods("POST")
def delete_product(request):
    """End point for deleting product.

    Args:
        request (POST)

    Request content: Expected content is a api token and a product id.
        in JSON type.

    Returns:
        HTTP Response: End point requires authentication, if successful,
            the product with the given id will be deleted.

            Forbidden (403): If not authenticated.
            Bad Request (400): No product with matching id.

            Response with product id as JSON type is returned if successful.
    """
    # Dummy authentication
    request_data = json.loads(request.body)
    if request_data.get('api_token') != 'token':
        return HttpResponseForbidden()
    product_id = request_data.get('product_id')
    try:
        Product.objects.get(id=product_id).delete()
    except ObjectDoesNotExist:
        return HttpResponseBadRequest()
    response_data = {'product_id': product_id}
    return HttpResponse(json.dumps(response_data),
                        content_type="application/json")
