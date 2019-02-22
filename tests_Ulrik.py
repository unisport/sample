import urllib.request
import urllib.parse
import os.path
import json


url = 'https://www.unisport.dk/api/sample/'
query = '?page=1&perpage=10'
subPath = ''
fullUrl = url + subPath + query



#class made to structure data from JSON properly
#For simplification this class only use the data necessary for this assignment
class ProductInfo:
    def __init__(self, productInfo):
        self.url = productInfo['url'] 
        self.relative_url = productInfo['relative_url']
        self.name = productInfo['name']
        self.ID = int(productInfo['id'])
        self.price = float(productInfo['price'].replace(',', '.'))
        self.currency = productInfo['currency']
        self.kids = int(productInfo['kids'])
        self.kid_adult = int(productInfo['kid_adult'])

    def IsProductAvailableForKids(self):
        if(self.kids or self.kid_adult):
            return True
        else:
            return False

def ReadUrl(url):
    attributes = urllib.parse.urlsplit(fullUrl)
    
    path2 = os.path.dirname(attributes.path)

    return attributes

def GetPageNumber(queryResult):
    if(queryResult['page'] is None):
            return 1
    else:
        return int(queryResult['page'][0])

def GetItemsPerPage(queryResult):
    if(queryResult['perpage'] is None):
        return 10
    else:
        return int(queryResult['perpage'][0])

def ParseToProductDataStructure(productList):
    productData = dict()
    #adds all products to the dict of all the products, using each product id, as its key, for easy lookup
    for currentProduct in productList:
        newProduct = ProductInfo(currentProduct)
        productData[newProduct.ID] = newProduct 

    return productData

def LoadData():
    with urllib.request.urlopen(url) as r:
        s = r.read().decode('utf-8')
    jsonData = json.loads(s)
    productData = ParseToProductDataStructure(jsonData['products'])
    return productData

def DisplayPage(url):
    productData = LoadData()

    categoryItems = list() #creating a list to be filled with items from the selected category

    attributes = ReadUrl(url)
    qres = urllib.parse.parse_qs(attributes.query)
    currentPage = os.path.split(attributes.path)
    page = GetPageNumber(qres)
    itemsPerPage = GetItemsPerPage(qres)
    #if we are on the products page show all items
    if(currentPage[0] == '/api/sample'):
        categoryItems = list(productData.values())
    elif(currentPage[0] != '/api/sample'):  #if we are not on the products page, but a subpage, clear all the items, and show selected ones instead
        categoryItems = []
        if(currentPage[0] == '/api/sample/id'):#id subpage
            urlID = int(currentPage[1])#casts read url to int, as the id has been saved as an int, but the url is read as a string
            product = productData.get(urlID)
            if(product is None):
                print('404: Url findes ikke')
                return False
            print('Det valgte produkt er:')
            DisplayItem(productData[urlID])
            return True
        elif(currentPage[0] == '/api/sample/kids'):#kids subpage
            print('Produkter til børn:')
            for selectedProduct in productData:
                if(productData[selectedProduct].IsProductAvailableForKids()):
                    categoryItems.append(productData[selectedProduct])  
        else:
            print('404: Url findes ikke')
            return False 
    else: #hvis url ikke er gyldig
       print('404: Url findes ikke')
       return False

    resultingItems = SortItemsForPageView(categoryItems, itemsPerPage, page)
    DisplayItems(resultingItems, page)
    return True

def SortItemsForPageView(dict, itemsPerPage, page):
    viewedItems = []

    lastItemIndex = len(dict)-1 #subtracting one to get the highest index
    pageNumberForCalc = max(0, min(page-1,lastItemIndex))#corrects the page number to be zeroIndexed for calculating item indexes
    startingItemIndex = int(pageNumberForCalc * itemsPerPage)
    endItemIndex = int(startingItemIndex + itemsPerPage)

    for x in range(startingItemIndex, endItemIndex):
        if(x > lastItemIndex): #if there are less items remaining than to fill a whole page, stop adding them to viewed list
            break
        viewedItems.append(dict[x])
    return viewedItems

def DisplayItem(displayItem):
    print('Genstand: ' + displayItem.name + ', Pris: ' + str(displayItem.price) + ' ' + displayItem.currency)

def DisplayItems(displayItems, pageNumber, itemsSorted = True):
    items = displayItems #creating list of the items to display, to either sort them, or not sort them
    itemAmountForPrint = str(len(items))
    if(itemsSorted):
        sortedByPrice = sorted(displayItems, key=lambda x: x.price)
        items = sortedByPrice
        print(itemAmountForPrint + ' produkter på side ' + str(pageNumber) + ' sorteret efter pris:')
    else:
        print(itemAmountForPrint + ' produkter på side ' + str(pageNumber) + ' usorteret:')

    for x in items:
        DisplayItem(x)
        

DisplayPage(url)

