from django.shortcuts import get_object_or_404, render
from django.http      import HttpResponseRedirect
from django.http      import HttpResponse, Http404
# from django.urls      import reverse not needed
from django.views     import generic

# for reading the sample json dump
import json
# for getting the data dump
from urllib.request import urlopen
################################################################################

def getJsonDataFromServer():
    # we use the testdata live from the server, in case they decide to change it
    try:
        jsonRequest = urlopen( 'https://www.unisport.dk/api/sample/' )
        jsonString  = jsonRequest.read().decode( 'utf-8' )
        return json.loads(jsonString)
    except:
        print( "failed to retrieve data from server." )
        return {'products': [{'name':"Failed to retrieve data from server."}] }


def products_sorted_by_price( items, index, amount ):
    #items = getJsonDataFromServer()['products']
    sorted_items = sorted( items,
                           key = lambda k:
                                float( k['price'].replace( ',', '.') ),
                           reverse = False )
    # The next if-else statement is to ensure that
    # the index won't go out of bounds
    if index >= len( sorted_items ):
        return [] # empty list
    elif index+amount >= len( sorted_items ):
        return sorted_items[index:]
    return sorted_items[index:index+amount]

def getProductByID( id ):
    for product in getJsonDataFromServer()['products']:
        if product['id'] == str(id):
            return product
    raise Http404

class IndexView( generic.ListView ):
    template_name       = 'products/index.html'
    context_object_name = 'jsonData'

    def get_page_number( self, request ):
        if ( 'page' in request.GET ):
            try:
                if int( request.GET['page'] ) > 0:
                    return int( request.GET['page'] )
            except: # we just return default(1) in case of exception
                print( "error: pagenumber is invalid" )
        return 1

    def get_queryset( self ):
        items    = getJsonDataFromServer()['products']
        page     = self.get_page_number( (self.request) )
        products = []

        # is this the kids subdirectory
        if self.request.path == '/products/kids/':
            tmp = []
            for p in items:
                # because there isn't any products with kids = 1
                # I added kid_adult. 2017-05-15
                if p['kid_adult'] == "1" or p['kids'] == "1":
                    tmp.append(p)
            items = tmp

        products = products_sorted_by_price( items,
                                             ( page - 1 ) * 10,
                                             10 )
        nxt = page + 1
        if len(products) < 10:
            nxt = page

        return {'products':products,
                'prev':page-1,
                'page':page,
                'next':nxt}

# it's sort-of hard to make a model containing a dict
# so I just used a function instead. easier but more code
def detail( product_id, item_list ):
    ID      = int( product_id )
    product = getProductByID( product_id )

    # in order for the navigation on the detailView to work
    # we need to map the ID's of the previous and the next item
    # on the sorted list
    nxt = 0
    prv = 0

    for i in range( 0, len( item_list ) ):
        if item_list[i]['id'] == product_id:
            if i < len( item_list ) - 1:
                nxt = int( item_list[i+1]['id'] )
            if i > 0:
                prv = int( item_list[i-1]['id'] )
    print("nxt: ", nxt, "\nprv: ", prv, "\n")
    return {'product':product,
            'id':ID,
            'next': nxt,
            'prev': prv}

def product_details(request, product_id):
    items = getJsonDataFromServer()['products']
    items = products_sorted_by_price( items, 0, 1024 ) # get all products
    return render(request, 'products/details.html', detail(product_id, items))

def kid_details(request, product_id):
    items = getJsonDataFromServer()['products']
    tmp   = []
    for p in items:
        # because there isn't any products with kids = 1
        # I added kid_adult. (2017-05-15)
        if p['kid_adult'] == "1" or p['kids'] == "1":
            tmp.append(p)
    items = products_sorted_by_price( tmp, 0, 1024 )
    return render(request, 'products/details.html', detail(product_id, items))
