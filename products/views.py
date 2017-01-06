import urllib2
import json
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404

RESPONSE = urllib2.urlopen('http://www.unisport.dk/api/sample/')
DATA = json.load(RESPONSE)['products']


def products(request):
    """
    renders the page with first 10 cheapest objects (same as with ?page=1)
    slices products and shows special 10 according to the page number if page get param exists
    """
    count = 10
    page = 1
    if 'page' in request.GET:
        page = int(request.GET['page'])
    template = 'products.html'
    return render_to_response(template, {'products': sorted(DATA, key=lambda x: float(x['price'].replace(',', '.')))[(page*count)-count:count*page]}, context_instance=RequestContext(request))


def kids(request):
    """
    renders the page with all the products where the kids key equals 1
    """
    template = 'kids.html'
    filtered_data = filter(lambda x: x['kids'] == '1', DATA)
    return render_to_response(template, {'products': sorted(filtered_data, key=lambda x: x['price'])}, context_instance=RequestContext(request))


def product(request, id):
    """
    renders page showing product with specific id.
    raises 404 if id does not exist
    """
    template = 'product.html'
    filtered_data = filter(lambda x: x['id'] == str(id), DATA)
    if not filtered_data:
        raise Http404
    return render_to_response(template, {'product': filtered_data[0]}, context_instance=RequestContext(request))


