from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import loader

from .models import Product


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
