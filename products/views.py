from django.http import HttpResponse
import requests
import json
import os


data_source = 'http://www.unisport.dk/api/sample/'


def get_data(cheapest=True, use_local=False):
    """
    Return the dictionary of products
    cheapest -- if True result will be sorted by price from cheapest (default True)
    use_local -- set True if you want to use local copy of sample.json, otherwise will use url from data_source variable (default True)
    """
    if not use_local:
        _response = requests.get(data_source)
        if _response.status_code == 200:
            data = json.loads(_response.text)
    # In case data source is unavailable we will use a local version of sample json
    else:
        data = json.loads(open(os.path.join(os.path.dirname(__file__),'sample.json')).read())
    if cheapest:
        # Lambda argument is a product dictionary. Price in the source has comma, so here we should replace it with dot.
        result = {'latest': sorted(data['latest'], key=lambda d: float(d[u'price'].replace(',', '.')))}
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

    data = get_data(cheapest=True)['latest']
    result = data[page * 10 - 10:page * 10]
    return HttpResponse(json.dumps(result), content_type="application/json")


def kids(request):
    """
    should return the products where kids=1 ordered with the cheapest first
    """
    data = get_data(cheapest=True)['latest']
    result = filter(lambda d: int(d[u'kids']) == 1, data)
    return HttpResponse(json.dumps(result), content_type="application/json")


def product(request, id):
    """
    should return the individual product.
    """
    data = get_data(cheapest=False)['latest']
    # There is a duplicate ids in json, so it's necessary to return just a first element
    result = filter(lambda d: d[u'id'] == id, data)[:1]
    return HttpResponse(json.dumps(result), content_type="application/json")