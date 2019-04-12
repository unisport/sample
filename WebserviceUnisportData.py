'''
Created on 9. apr. 2019

@author: Lars Jespersen
@contains: webservice checks the url for variables and routes the request. Return the data as json 
'''
from SortData import SortData
from GetData import GetData
from ManipulateData import ManipulateData

import json

from flask import request
from flask import Flask
app = Flask(__name__)

try:
    #catch the base url and return all products
    @app.route('/')
    def defaultRequest():
        oGetData = GetData()
        oUnisportData = oGetData.GetUnisportData()
        
        oSortData = SortData()
        oSortedData = oSortData.sortByPrice(oUnisportData, True)
        #convert the list back to json
        return json.dumps(oSortedData)
    
    @app.route('/products/')
    def productsRequest():
        oGetData = GetData()
        oUnisportData = oGetData.GetUnisportData()
        
        oSortData = SortData()
        oSortedData = oSortData.sortByPrice(oUnisportData, False)
        
        iPageVar = str(request.args.get('page'))
        #test if the page value only contains numbers
        if not (iPageVar.isdigit()):
            iPageVar="1"
        #paginate the result to only show 10 pr page
        oPage= oSortData.paginateList(oSortedData, iPageVar, 10)
        
        #oPage = paginate.Page(oSortedData,page=iPageVar,items_per_page=10)
        #convert the list back to json
        return json.dumps(oPage)
    
    #since the sample data does not contain the key "kids", 
    #i test if the key "name" of the product contains the string "Børn" to get the products
    @app.route('/products/kids/')
    def productsKidsRequest():
        oGetData = GetData()
        oUnisportData = oGetData.GetUnisportData()
        
        oSortData   = SortData()
        oSortedData = oSortData.getDictsByStringInKeyValue(oUnisportData, "name", "Børn")
        #paginate the result to only show 10 pr page,         #paginate the result to only show 10 pr page
        iPageVar=1
        #paginate the result to only show 10 pr page
        oPage= oSortData.paginateList(oSortedData, iPageVar, 10)
        #convert the list back to json
        return json.dumps(oPage)
    
    #the format of the url is /products/id/xxxx where xxxx is the id 
    @app.route('/products/id/<iProductId>/')
    def productIdRequest(iProductId):
        oGetData = GetData()
        oUnisportData = oGetData.GetUnisportData()
            
        if not (iProductId.isdigit()):
            return "Product value should only contain numbers"
            
        oSortData = SortData()
        oSortedData = oSortData.getSpecificDictById(oUnisportData, int(iProductId))
    
        #convert the list back to json
        return json.dumps(oSortedData)
    
    #the format of the url is /products/delete/id/xxxx where xxxx is the id 
    @app.route('/products/delete/id/<iProductId>/')
    def productDeleteIdRequest(iProductId):
        oGetData = GetData()
        oUnisportData = oGetData.GetUnisportData()
            
        if not (iProductId.isdigit()):
            return "Product value should only contain numbers"
            
        oManipulateData = ManipulateData()
        oSortedData = oManipulateData.deleteProductById(oUnisportData, int(iProductId))
    
        #convert the list back to json
        return json.dumps(oSortedData)
    
    #the format of the url is /products/update/id/xxxx/key/yyyy/value/zzzz 
    #where xxxx is the id, where yyyy is the name of the key to be updated, where zzzz is the value to be inserted
    @app.route('/products/update/id/<iProductId>/key/<sKey>/value/<sValue>/')
    def productUpdateIdRequest(iProductId,sKey,sValue):
        oGetData = GetData()
        oUnisportData = oGetData.GetUnisportData()
            
        if not (iProductId.isdigit()):
            return "Product value should only contain numbers"
            
        oManipulateData = ManipulateData()
        oSortedData = oManipulateData.updateProductById(oUnisportData, int(iProductId), sKey, sValue)
    
        #convert the list back to json
        return json.dumps(oSortedData)   

    #take json data which holds all the information which is sample in the sample data and insert the product and return the new unisport sample data   
    @app.route('/products/create/', methods=['POST'])
    def productCreateRequest():
        oGetData = GetData()
        oUnisportData = oGetData.GetUnisportData()

        if not request.json:
            return "json data not valid"           
        
        oNewProduct = json.loads(request.json)    
        oManipulateData = ManipulateData()
        oSortedData = oManipulateData.createProduct(oUnisportData, oNewProduct)
    
        #convert the list back to json
        return json.dumps(oSortedData)    
         
except:
    print('An error have occured')
    
if __name__ == '__main__':
    app.run(debug=True)

