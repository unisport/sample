import json

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.core.serializers.json import DjangoJSONEncoder
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect
import requests

from products import data_source
from products.models import Product, SourceSettings, Size


def get_data(cheapest=True):
    """
    Return the dictionary of products
    cheapest -- if True result will be sorted by price from cheapest (default True)
    """

    # use_local settings stored in product_sourcesettings table
    # if True then will use local database, otherwise will use url from data_source variable
    use_local = SourceSettings.objects.get(name="use_local").value

    # Just in case if nor local nor remote data is available
    data = None

    if not use_local:
        _response = requests.get(data_source)
        if _response.status_code == 200:
            data = json.loads(_response.text).get('latest', [])
        else:
            # In case data source is unavailable we will use a local version of sample json
            use_local = True
    if use_local:
        # If product list will be big it's better to filter and sort everything in django query.
        # It selects all objects in order to be able to use both local and remote data sources.
        data = Product.objects.all().values()

    if cheapest and data:
        # Lambda argument is a product dictionary. Price in the source has comma, so here we should replace it with dot.
        result = sorted(data,
                        key=lambda d: float(
                            d[u'price'].replace(',', '.') if isinstance(d[u'price'], unicode) else d[u'price']))
        return result
    return data


def products(request, page=1):
    """
    should return the first 10 objects ordered with the cheapest first.
    /?page=2
    The products should be paginated where page in the url above should return the next 10 objects
    pare -- number of the page (default 1)
    """
    page_string = request.GET.get('page')
    # In case we have page in query parameters.
    if page_string:
        page = int(page_string)

    data = get_data(cheapest=True)
    result = data[page * 10 - 10:page * 10]
    return HttpResponse(json.dumps(result, cls=DjangoJSONEncoder), content_type="application/json")


def kids(request):
    """
    should return the products where kids=1 ordered with the cheapest first
    """
    data = get_data(cheapest=True)
    result = filter(lambda d: int(d[u'kids']) == 1, data)
    return HttpResponse(json.dumps(result), content_type="application/json")


def product(request, id):
    """
    should return the individual product.
    """
    data = get_data(cheapest=False)
    # There is a duplicate ids in json, so it's necessary to return just a first element
    result = filter(lambda d: d[u'id'] == id, data)[:1]
    return HttpResponse(json.dumps(result), content_type="application/json")


@staff_member_required
def import_data(request):
    # After import use_local should be checked in order to use local stored data
    use_local = SourceSettings.objects.get(name="use_local")
    use_local.value = False
    use_local.save()
    for item in get_data():
        sizes = item.pop('sizes', '').split(',')
        for size in sizes:
            size_instance = Size(size=size)
            try:
                size_instance.save()
            # If size is already exists IntegrityError will be raised. Don't raise error here because it's not a problem
            except IntegrityError:
                pass

        # All duplicated products from remote data set will be rewrited
        product_instance = Product(**item)
        product_instance.save()
        product_instance.sizes.add(*(Size.objects.get(size=size) for size in sizes))
        product_instance.save()

    use_local.value = True
    use_local.save()
    messages.add_message(request, messages.INFO, 'Data has been imported. Use_local was set')
    return redirect(request.META['HTTP_REFERER'], messages)