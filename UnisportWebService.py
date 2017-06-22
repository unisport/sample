# Christo Matrakou
# 21/06/2017
# This is my first attempt programming in python!!!

# Web Service
# Service runs on http://localhost + url from the urls

# import of the neccessary libraries and modules used in the service
import urllib.request
from urllib.parse import urlparse
import web
import json
from operator import itemgetter
from collections import OrderedDict
import operator
from decimal import Decimal
from re import sub

# getting the data from the url
# sort the products in the dictionary by price only once.
# running time of method is O(n logn)
# This way every time we need the 10 cheapest or 5 cheaptest etc just retrieve from list
# according to position
# converts the price temporarely to decimal for sorting because cannot use type string to sort
with urllib.request.urlopen("https://www.unisport.dk/api/sample/") as url:
            data = json.loads(url.read().decode())
data['products'].sort(key=lambda x:Decimal(sub(r'[^\d.]', '', x['price'])))

# Paginate products in a dictionary
# Used a dict() with the key being the page number that holds all the products
# in ascending price. This takes linear time and saves times for later use
# in returning products of specific page by constant access to the dict_pages 
dict_pages=dict()
paged=1
list_page=[]
for i in range(0,len(data['products'])):
    list_page.append(data['products'][i])
    if(i%10==9):
        dict_pages[paged]=list_page
        paged=paged+1
        list_page=[]
if(len(list_page)>0):
    dict_pages[paged]=list_page
          
#print("data parsed")
#print (json.dumps(data, indent=4, sort_keys=True))
#print(data["products"][1]["id"])

# the 4 urls for outputing the data required 
urls=('/products','get_products',
      '/products/kids/','get_products_kids',
      '/products/' ,'get_page',
      '/products/(.*)/','get_id')


# returns the 10 cheapest products
# instead of going through the products by using the dict_pages[1]
# the 10 cheapest products are returned in constant time.
class get_products:
    def GET(self):
        return dict_pages[1]
        #print(output)


# returns all the products where 'kids' = '1'
class get_products_kids:
    def GET(self):
        kids_list=[]
        for val in data["products"]:
            if(val["kids"]=="1"):
                kids_list.append(val)
        return kids_list


# returns the product of a specific 'id'
# worst case is in linear time by iteerating through the products until finding the one with this id
# it could run in logn time if products where sorted by id
class get_id:
    def GET(self,id):
         for val in data["products"]:
            if(val["id"]==id):
                return val

            
# returns the products of a page passed as a query to the url
# using the dict_pages the performance is improved to run in constant time
class get_page():
    def GET(self):
      try:
        i = web.input(page = 'web')
        page_number=int(web.websafe(i.page))
      except Exception:
          return 'Invalid page number'
      else:
          if page_number in dict_pages.keys():
              return(dict_pages[page_number])
          else:
              return 'Page does not exist!'
        



if __name__ == "__main__":
    app = web.application(urls, globals(),True)
    app.run()


