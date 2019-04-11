import json

# using cherrypy as webserver
import cherrypy
# using request to fetch data
import requests


class ProductHandler(object):
    def __init__(self):
        # get sample products when object is initialized
        stream = requests.get('https://www.unisport.dk/api/sample/')
        jsonStream = json.loads(stream.text)
        self.products = jsonStream['products']
        # sort the list by cheapest
        self.products = sorted(self.products, key=lambda k: float(k['price']))
   
    def getProducts(self, page = 1):
        result = {'products': []}
        i = 0
        s = (int(page)-1) * 10

        # loop to add the next ten items to result
        for x in self.products:
            if i >= (s + 10):
                break
            if i >= s:
                result['products'].append(x)
            i += 1

        # error handling if no products were found
        if not result['products']:
            return {'status': 'No kids items found'}
        return result
    
    def getKidsProducts(self, page = 1):
        result = {'products': []}
        i = 0
        s = (int(page)-1) * 10

        # loop to add the next ten items to result
        for x in self.products:
            if 'kids' in x and x['kids'] == 1:
                if i >= (s + 10):
                    break
                if i >= s:
                    result['products'].append(x)
                i += 1
        # error handling if no products were found
        if not result['products']:
            return {'status': 'No kids items found'}
        return result

    def getProductById(self, id):
        # loop through items, return
        for x in self.products:
            if x['id'] == id:
                return x

        # error handling if no product was found   
        return {'status': 'Item not found'}

        
class RoutingProducts(object):
    @cherrypy.expose
    def index(self, page = 1):
        ph = ProductHandler()
        output = ph.getProducts(page)
        return json.dumps(output)
    
    @cherrypy.expose
    def kids(self, page = 1):
        ph = ProductHandler()
        output = ph.getKidsProducts(page)
        return json.dumps(output)

    @cherrypy.expose
    def id(self, *args):
        ph = ProductHandler()
        output = ph.getProductById(args[0])
        return json.dumps(output)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def create(self):
        # handle data sent over
        data = cherrypy.request.json
        # verify required fields are filled out
        # save to db
        # return success/error
        return data

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def update(self):
        data = cherrypy.request.json
        # handle data sent over
        # verify required fields are filled out
        # update db
        # return success/error
        return data
    
    @cherrypy.expose
    def delete(self, *args):
        data = cherrypy.request.json
        # verify args[] is valid product id
        # remove from db
        # return success/error
        return data
        

class ProductWebService(object):
    def __init__(self):
        self.products = RoutingProducts()


if __name__ == '__main__':
    config = {
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 8080
        }
    # config should extend to some user authentication, especially regarding the bonus functions
    cherrypy.config.update(config)
    cherrypy.quickstart(ProductWebService())
