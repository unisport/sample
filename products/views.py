from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from products import domain
from products.decorators import error_on_exception
from products.encoders import ProductEncoder


@error_on_exception
def products(request):
    page = int(request.GET.get('page', 1))
    data = domain.get_products_page(page=page, limit=10)
    return JsonResponse({
        'data': data,
    }, encoder=ProductEncoder)


@error_on_exception
def kids_products(request):
    page = int(request.GET.get('page', 1))
    data = domain.get_products_page(page=page, limit=10)
    return JsonResponse({
        'data': data,
    }, encoder=ProductEncoder)


@error_on_exception
def product_by_id(request, product_id):
    try:
        product = domain.get_product_by_id(product_id)
        return JsonResponse({
            'data': product,
        }, encoder=ProductEncoder)
    except ObjectDoesNotExist:
        return JsonResponse({
            'error': {
                'message': ('Product with id={} does not exist.'
                            .format(product_id))
            },
        }, status=404)
