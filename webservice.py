import os
import json
import urllib2

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/products/kids/')
def getKids():
    """return the products where kids=1 ordered with the cheapest first"""
    data = getJsonFromSample()
    sortedProducts = sortJsonListCheapestFirst(data['products'])

    #kidProducts = []
    #for product in sortedProducts:
    #    if product['kids'] == '1':
    #       kidProducts.append(product)
        
    #data['products'] = kidProducts
    
    data['products'] = filter(lambda product: product['kids'] == '1', data['products']) # Using the filter method insted of the above, to avoide manualy checking every entry with a loop.
    data['end-point'] = '/products/kids/'
    
    return jsonify(data)


@app.route('/products/')
def getProductsByPage():
    """returning 10 products coresponding to page."""
    print(request.args.get('page'))
    pageNo = 1  # default value will be used when no args is passed allong
    if not request.args.get('page') == None:
        pageNo = int(request.args.get('page'))
    
    print('page: %s' % pageNo)  # for some resone page comes back with a value of 1 no matter what I do.
    productsPerPage = 10    # Controlles number of products per page
    data = getJsonFromSample()
    sortedProducts = sortJsonListCheapestFirst(data['products'])
    countModifier = productsPerPage * (pageNo - 1)    # adjust the count to get the next set of products according to pagecount.
    print('countModifier: %s' % countModifier)
    
    productRange = productsPerPage
    print('Length of sortedProducts: %s' % len(sortedProducts))
    if len(sortedProducts)-countModifier < 10:
        productRange = len(sortedProducts)-countModifier    # making sure not getting out of bound if less then 10 products left on requested page.
        print('inside if, productRange new value: %s' % productRange)
    pagedProducts = []
    if productRange > 0:    # making sure not running zero or a negative number, because as is, you can request a page long past the last product. This way it will return an empty list.
        for x in range(productRange):
            pagedProducts.append(sortedProducts[x+countModifier])
        
    data['products'] = pagedProducts
    if pageNo == 1:
        data['end-point'] = '/products/'
    else:
        data['end-point'] = '/products/?page=%s' % pageNo
        
    return jsonify(data)
    
    
@app.route('/products/<int:productId>/')
def getProductsById(productId):
    """return the individual product."""
    
    data = getJsonFromSample()
    data['products'] = filter(lambda product: int(product['id']) == productId, data['products'])
    #Using this method, because we trust id should be unique. In case there should be more with the same id, they should all be included.
    
    data['end-point'] = '/products/%d' % productId
    return jsonify(data)
    
    
def getJsonFromSample():
    """Returns a JSON object from an url"""
    req = urllib2.Request("http://www.unisport.dk/api/sample/")
    opener = urllib2.build_opener()
    f = opener.open(req)
    data = json.loads(f.read())
    return data


def sortJsonListCheapestFirst(jsonList):
    """Sorts a JSON array cheapest first."""
    return sorted(jsonList, key=lambda k: float(k['price'].replace(',','.')), reverse=False) #Using the replace function, in order to make the strings readable as floats.
    
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080))) # using http://0.0.0.0:8080/ so it will work in Cloud9.
