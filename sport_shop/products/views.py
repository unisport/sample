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
def listing_products(request):
    # All products ordered by price
    all_products = Product.objects.order_by('price').all()
    # Default pagination is 10 products per page
    products_per_page = request.GET.get('products_per_page', 10)
    paginator = Paginator(all_products, products_per_page)
    template = loader.get_template('products/listing_products.html')
    page = request.GET.get('page', 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = 1
        products = paginator.page(page)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page = paginator.num_pages
        products = paginator.page(page)
    try:
        prev_page = products.previous_page_number()
    except EmptyPage:
        prev_page = None
    try:
        next_page = products.next_page_number()
    except EmptyPage:
        next_page = None
    context = {
        'products': products,
        'pages_info': {
            'current': page,
            'count': paginator.num_pages,
            'previous': prev_page,
            'next': next_page,
        }
    }
    return HttpResponse(template.render(context, request))


@csrf_exempt
@require_http_methods("POST")
def create_product(request):
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
