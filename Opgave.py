import json
import urllib2
import requests
from flask import Flask, jsonify
import unittest


##################################### Help def ###################################################
def getDataFromURL(): # Loads data from url.
    requestURL = urllib2.Request("http://www.unisport.dk/api/sample/")
    openurl = urllib2.build_opener()
    temp = openurl.open(requestURL)
    data = json.loads(temp.read())
    return data

def SortListCheapest(dataList): # Sort the data as list according to price. Cheapest first
    return sorted(dataList, key=lambda k: float(k['price'].replace(',','.')), reverse=False)


# Use this def to test the output for (/products/?page=2), as the webpage implementation unfortunately did not work.
def ProductsByPageNoWeb(pageNumber):
    outputList = []
    data = getDataFromURL()
    SortedList2 = SortListCheapest(data['products'])
    
    if pageNumber == 1:
        for ii in range(10,20):
            outputList.append([SortedList2[ii]['price'],SortedList2[ii]['name']])
    elif pageNumber == 2:
        for ii in range(10,20):
            outputList.append([SortedList2[ii]['price'],SortedList2[ii]['name']])
    elif pageNumber == 3:
        for ii in range(20,len(SortedList2)):
            outputList.append([SortedList2[ii]['price'],SortedList2[ii]['name']])

    # The above if statements could have been made using a for-loop, but as the data set is small
    # the above method is used instead.

    return outputList

print ProductsByPageNoWeb(2) # Outputs the result of the task 3. Output in terminal.


################################## Web ###########################################################

app = Flask(__name__)

#10 Cheapest products
@app.route('/products/')
def getListOf10CheapestProducts():
    Cheapest10Prod = []
    data = getDataFromURL()
    SortedList = SortListCheapest(data['products'])
    
    for i in range(0,len(SortedList)):
        Cheapest10Prod.append([SortedList[i]['price'],SortedList[i]['name']])
    
    output = Cheapest10Prod[0:10]

    return json.dumps(output)

#Kids True
@app.route('/products/kids')
def ListOfKids():
    data = getDataFromURL()
    SortedList = SortListCheapest(data['products'])
    ListKidsTrue = []
    for i in range(0,len(SortedList)):
        if SortedList[i]['kids'] == "1":
            ListKidsTrue.append([SortedList[i]['price'],SortedList[i]['name']])

    if len(ListKidsTrue) == 0:
        return 'The list is empty, no products where kids=1'
    elif len(ListKidsTrue) >= 1:
        return json.dumps(ListKidsTrue)

#Page 2 The below code was the inteded for the third task
@app.route('/products/?page=2')
def ProductsByPage():
    outputList = []
    data = getDataFromURL()
    SortedList2 = SortListCheapest(data['products'])
    
    if pageNumber == 1:
        for ii in range(10,20):
            outputList.append([SortedList2[ii]['price'],SortedList2[ii]['name']])
    elif pageNumber == 2:
        for ii in range(10,20):
            outputList.append([SortedList2[ii]['price'],SortedList2[ii]['name']])
    elif pageNumber == 3:
        for ii in range(20,len(SortedList2)):
            outputList.append([SortedList2[ii]['price'],SortedList2[ii]['name']])

    return json.dumps(outputList)

#Product by ID
@app.route('/products/<UniqueID>/')
def ProductByID(UniqueID):
    data = getDataFromURL()
    ProByID = []
    for i in range(0,len(data['products'])):
        if data['products'][i]['id'] == UniqueID:
            ProByID.append(data['products'][i]['name'])

    if len(ProByID) == 0:
        return 'The given ID is not a product'
    elif len(ProByID) >= 1:
        return json.dumps(ProByID)

if __name__=="__main__":
    app.run()



