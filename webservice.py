#importing libraries
import web
import json	
import requests

#fethcing the data from url and writing them to a json file
response = requests.get("https://www.unisport.dk/api/sample/")
with open('data.json', 'w') as f:
     json.dump(response.json(), f)
     
# open the json file and pass the data to "data" variable
with open('data.json', 'r') as f:
            data = json.load(f)

#defining the urls and the corresponding classes names
urls = (
    '/products/?','pages',
    '/products/kids/', 'kids',
    '/products/(\d+)/', 'product_id',
)

app = web.application(urls, globals())   

class kids:
    def GET(self):
        """Returns the products where kids=1 ordered with the cheapest first"""
        kid_products = data["products"] 
        #sorting all the products by ascending price
        kid_products = sorted(kid_products, key=lambda x: float(x['price'].replace(",",""))) 
        #creating list with products where kids=1
        kid_products = [product for product in kid_products if product["kids"]=="1"] 
        #encoding back to json  
        kid_products = json.dumps(kid_products)
        #returning the json with ascending price and kids=1
        return kid_products

class pages:
    def GET(self):
        """1) Returns the first 10 objects ordered with the cheapest first.
           2) Return the products according to the page number"""    
        #user input after /products/? is returned as a key:value pair in a dictionary i.
        i = web.input()
        #If the dict is empty that corresponts to /products/ and 
        #10 objects ordered with the cheapest first are returned.
        if len(i.keys())==0 :
            products=data["products"]
            products = sorted(products, key=lambda x: float(x['price'].replace(",",""))) 
            # keep the 10 fisrt products            
            products = {"products":products[:10]}
            products = json.dumps(products)
            return products
        # otherwise pagination occurs with 10 items per page        
        page = int(i["page"])
        #products is an array and can be sliced
        products = data["products"] 
        #Constant to select the number of items per page
        PRODUCTS_PER_PAGE = 10 
        total_products = len(products)
        maxpage = total_products/PRODUCTS_PER_PAGE
        
        if total_products%PRODUCTS_PER_PAGE > 0:           
            maxpage+=1
        if page > maxpage:
            return "Error! Inserted page is out of range!"
        #user insert page number at least = 1
        if page == 0:
            return "Invalid page number, pages start at 1!" 
        #defining the limits for slicing
        start_index = (page-1) * PRODUCTS_PER_PAGE;
        end_index = (page-1) * PRODUCTS_PER_PAGE+PRODUCTS_PER_PAGE;
        return json.dumps(products[start_index:end_index])        
                     
class product_id:
    def GET(self, id_number):
        """Returns the product by id"""
        products = data["products"]
        product = [product for product in products if int(product["id"])==int(id_number)]
        product = json.dumps(product)
        return product
        
if __name__ == "__main__":
    app.run()

#To avoid kicking off web.py's webserver while testing the following can be used :

#import os
#def is_test():
#    if 'WEBPY_ENV' in os.environ:
#        return os.environ['WEBPY_ENV'] == 'test'
#
#if (not is_test()) and __name__ == "__main__":     
#    app.run()     