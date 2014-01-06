import wsgiref.util 
import sys
import os
import json

sys.path.append(os.path.dirname(__file__))
from Product import Product
import ProductLoader
import ModeGetter
from ProductJsonEncoder import ProductJsonEncoder

def toJson(objects):
    return json.dumps(objects, cls=ProductJsonEncoder)

def application(environ, start_response):
    status = '200 OK'

    requestUri = wsgiref.util.request_uri(environ)

    mode = ModeGetter.getMode(requestUri)
    if mode == 2:
         productId = ModeGetter.getProductId(requestUri)
         product = ProductLoader.getProductById(productId)
         output = toJson(product)
    elif mode == 1:
         pageNumber = ModeGetter.getPageNumber(requestUri)
         kidsProducts = ProductLoader.productsKidsOnlySortedByPriceAsc(pageNumber)
         output = toJson(kidsProducts)
    else:
         pageNumber = ModeGetter.getPageNumber(requestUri)
         products = ProductLoader.productsSortedByPriceAsc(pageNumber)
         output = toJson(products)

    response_headers = [('Content-type', 'application/json;charset=utf-8'), ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
