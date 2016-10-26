import json
from Product import Product

def loadAllProducts():
    jsonProducts = json.loads('{"latest": [{"kids": "1", "name": "Nike - Spilletr\u00f8je Classic III B\u00f8rn R\u00f8d/Hvid", "sizes": "140-152 cm/Boys M,152-158 cm/Boys L,158-170 cm/Boys XL", "url": "http://www.unisport.dk/fodboldudstyr/nike-spilletroje-classic-iii-born-rodhvid/50626/", "free_porto": "0", "price": "134,00", "package": "0", "delivery": "5-14 dage", "kid_adult": "0", "price_old": "179,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/50626_mellem.jpg", "id": "50626", "women": "0"}, {"kids": "1", "name": "Puma - Spilletr\u00f8je Vencida Bl\u00e5 B\u00f8rn TILBUD", "sizes": "YXS/116 cm,YM/140 cm,YXL/164 cm", "url": "http://www.unisport.dk/fodboldudstyr/puma-spilletroje-vencida-bla-born-tilbud/59954/", "free_porto": "0", "price": "99,00", "package": "0", "delivery": "1-2 dage", "kid_adult": "0", "price_old": "199,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/59954_mellem.jpg", "id": "59954", "women": "0"}, {"kids": "1", "name": "Puma - Spilletr\u00f8je Vencida Hvid/Bl\u00e5 B\u00f8rn TILBUD", "sizes": "YXS/116 cm,YM/140 cm,YXL/164 cm", "url": "http://www.unisport.dk/fodboldudstyr/puma-spilletroje-vencida-hvidbla-born-tilbud/59961/", "free_porto": "0", "price": "99,00", "package": "0", "delivery": "1-2 dage", "kid_adult": "0", "price_old": "199,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/59961_mellem.jpg", "id": "59961", "women": "0"}, {"kids": "1", "name": "Puma - Shorts Vencida II Bl\u00e5 B\u00f8rn TILBUD", "sizes": "YXS/116 cm,YXL/164 cm", "url": "http://www.unisport.dk/fodboldudstyr/puma-shorts-vencida-ii-bla-born-tilbud/59972/", "free_porto": "0", "price": "79,00", "package": "0", "delivery": "1-2 dage", "kid_adult": "0", "price_old": "159,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/59972_mellem.jpg", "id": "59972", "women": "0"}, {"kids": "1", "name": "Adidas - F10 AdiZero FG Bl\u00e5/Lilla/Hvid B\u00f8rn ", "sizes": "EU 32,EU 33,EU 36/UK 3\u00bd,EU 36\u2154/UK 4,EU 37\u2153/UK 4\u00bd,EU 38/UK 5,EU 38\u2154/UK 5\u00bd", "url": "http://www.unisport.dk/fodboldstoevler/adidas-f10-adizero-fg-blalillahvid-born/95763/", "free_porto": "0", "price": "199,00", "package": "0", "delivery": "1-2 dage", "kid_adult": "0", "price_old": "399,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/95763_mellem.jpg", "id": "95763", "women": "0"}, {"kids": "1", "name": "Macron - Spilles\u00e6t Raven Hvid/Sort B\u00f8rn", "sizes": "140/2XS,152/X-Small", "url": "http://www.unisport.dk/fodboldudstyr/macron-spillesaet-raven-hvidsort-born/65458/", "free_porto": "0", "price": "199,00", "package": "0", "delivery": "4-8 dage", "kid_adult": "0", "price_old": "349,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/65458_mellem.jpg", "id": "65458", "women": "0"}, {"kids": "1", "name": "Macron - Spilles\u00e6t Trend Bordeaux/Hvid B\u00f8rn", "sizes": "116/3XS,140/2XS,152/X-Small", "url": "http://www.unisport.dk/fodboldudstyr/macron-spillesaet-trend-bordeauxhvid-born/65478/", "free_porto": "0", "price": "229,00", "package": "0", "delivery": "4-8 dage", "kid_adult": "0", "price_old": "349,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/65478_mellem.jpg", "id": "65478", "women": "0"}, {"kids": "1", "name": "Macron - Spilles\u00e6t Trend R\u00f8d/Sort B\u00f8rn", "sizes": "116/3XS,140/2XS,152/X-Small", "url": "http://www.unisport.dk/fodboldudstyr/macron-spillesaet-trend-rodsort-born/65480/", "free_porto": "0", "price": "229,00", "package": "0", "delivery": "4-8 dage", "kid_adult": "0", "price_old": "349,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/65480_mellem.jpg", "id": "65480", "women": "0"}, {"kids": "1", "name": "Macron - Spilles\u00e6t Trend Navy/R\u00f8d B\u00f8rn", "sizes": "116/3XS,140/2XS,152/X-Small", "url": "http://www.unisport.dk/fodboldudstyr/macron-spillesaet-trend-marinerod-born/65481/", "free_porto": "0", "price": "229,00", "package": "0", "delivery": "4-8 dage", "kid_adult": "0", "price_old": "299,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/65481_mellem.jpg", "id": "65481", "women": "0"}, {"kids": "0", "name": "Italien - Track Top 70 Italia Copa", "sizes": "Small,Medium,Large,X-Large,XX-Large", "url": "http://www.unisport.dk/fodboldtroejer/italien-track-top-70-italia-copa/24421/", "free_porto": "0", "price": "599,00", "package": "0", "delivery": "5-10 dage", "kid_adult": "0", "price_old": "599,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/24421_mellem.jpg", "id": "24421", "women": "0"}, {"kids": "0", "name": "Puma - King Top DI FG ", "sizes": "EU 38/UK 5,EU 38\u00bd/UK 5\u00bd,EU 39/UK 6,EU 40/UK 6\u00bd,EU 40\u00bd/UK 7,EU 41/UK 7\u00bd,EU 42/UK 8,EU 42\u00bd/UK 8\u00bd,EU 43/UK 9,EU 44/UK 9\u00bd,EU 44\u00bd/UK 10,EU 45/UK 10\u00bd,EU 46/UK 11,EU 46\u00bd/UK 11\u00bd", "url": "http://www.unisport.dk/fodboldstoevler/puma-king-top-di-fg/26487/", "free_porto": "0", "price": "699,00", "package": "0", "delivery": "1-2 dage", "kid_adult": "0", "price_old": "999,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/26487_mellem.jpg", "id": "26487", "women": "0"}, {"kids": "0", "name": "Sells - M\u00e5lmandsbukser Supreme", "sizes": "X-Large", "url": "http://www.unisport.dk/maalmandshandsker/sells-malmandsbukser-supreme/28683/", "free_porto": "0", "price": "299,00", "package": "0", "delivery": "1-2 dage", "kid_adult": "0", "price_old": "349,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/28683_mellem.jpg", "id": "28683", "women": "0"}, {"kids": "0", "name": "Nike - Vest 10 stk Gr\u00f8n", "sizes": "Small/Medium,Large/X-Large", "url": "http://www.unisport.dk/fodboldudstyr/nike-vest-10-stk-gron/45357/", "free_porto": "0", "price": "679,00", "package": "0", "delivery": "5-14 dage", "kid_adult": "0", "price_old": "799,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/45357_mellem.jpg", "id": "45357", "women": "0"}, {"kids": "0", "name": "Hummel - Polo Corporate Basic Hvid", "sizes": "X-Small,Large,X-Large", "url": "http://www.unisport.dk/fodboldudstyr/hummel-polo-corporate-basic-hvid/48286/", "free_porto": "0", "price": "129,00", "package": "0", "delivery": "5-10 dage", "kid_adult": "0", "price_old": "299,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/48286_mellem.jpg", "id": "48286", "women": "0"}, {"kids": "1", "name": "Nike - Spilletr\u00f8je Classic III B\u00f8rn R\u00f8d/Hvid", "sizes": "140-152 cm/Boys M,152-158 cm/Boys L,158-170 cm/Boys XL", "url": "http://www.unisport.dk/fodboldudstyr/nike-spilletroje-classic-iii-born-rodhvid/50626/", "free_porto": "0", "price": "134,00", "package": "0", "delivery": "5-14 dage", "kid_adult": "0", "price_old": "179,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/50626_mellem.jpg", "id": "50626", "women": "0"}, {"kids": "0", "name": "Select - Fodboldstr\u00f8mper Italia Sort", "sizes": "28-32,33-36,37-41,42-47", "url": "http://www.unisport.dk/fodboldudstyr/select-fodboldstromper-italia-sort/51126/", "free_porto": "0", "price": "59,00", "package": "0", "delivery": "4-8 dage", "kid_adult": "1", "price_old": "69,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/51126_mellem.jpg", "id": "51126", "women": "0"}, {"kids": "0", "name": "Select - Fodboldstr\u00f8mper Italia Hvid", "sizes": "28-32,33-36,37-41,42-47", "url": "http://www.unisport.dk/fodboldudstyr/select-fodboldstromper-italia-hvid/51127/", "free_porto": "0", "price": "59,00", "package": "0", "delivery": "4-8 dage", "kid_adult": "1", "price_old": "69,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/51127_mellem.jpg", "id": "51127", "women": "0"}, {"kids": "0", "name": "Select - Fodboldstr\u00f8mper Italia Bl\u00e5", "sizes": "28-32,33-36,37-41,42-47", "url": "http://www.unisport.dk/fodboldudstyr/select-fodboldstromper-italia-bla/51128/", "free_porto": "0", "price": "59,00", "package": "0", "delivery": "4-8 dage", "kid_adult": "1", "price_old": "69,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/51128_mellem.jpg", "id": "51128", "women": "0"}, {"kids": "0", "name": "Select - Fodboldstr\u00f8mper Italia Gr\u00f8n", "sizes": "28-32,33-36,37-41,42-47", "url": "http://www.unisport.dk/fodboldudstyr/select-fodboldstromper-italia-gron/51129/", "free_porto": "0", "price": "59,00", "package": "0", "delivery": "4-8 dage", "kid_adult": "1", "price_old": "69,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/51129_mellem.jpg", "id": "51129", "women": "0"}, {"kids": "0", "name": "Select - Fodboldstr\u00f8mper Italia Lysebl\u00e5", "sizes": "28-32,33-36,37-41,42-47", "url": "http://www.unisport.dk/fodboldudstyr/select-fodboldstromper-italia-lysebla/51130/", "free_porto": "0", "price": "59,00", "package": "0", "delivery": "4-8 dage", "kid_adult": "1", "price_old": "69,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/51130_mellem.jpg", "id": "51130", "women": "0"}, {"kids": "0", "name": "Select - Fodboldstr\u00f8mper Italia Navy", "sizes": "28-32,33-36,37-41,42-47", "url": "http://www.unisport.dk/fodboldudstyr/select-fodboldstromper-italia-navy/51131/", "free_porto": "0", "price": "59,00", "package": "0", "delivery": "4-8 dage", "kid_adult": "1", "price_old": "69,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/51131_mellem.jpg", "id": "51131", "women": "0"}, {"kids": "0", "name": "Select - Fodboldstr\u00f8mper Italia R\u00f8d", "sizes": "28-32,33-36,37-41,42-47", "url": "http://www.unisport.dk/fodboldudstyr/select-fodboldstromper-italia-rod/51132/", "free_porto": "0", "price": "59,00", "package": "0", "delivery": "4-8 dage", "kid_adult": "1", "price_old": "69,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/51132_mellem.jpg", "id": "51132", "women": "0"}, {"kids": "0", "name": "Select - Fodboldstr\u00f8mper Italia Bl\u00e5/hvid", "sizes": "28-32,33-36,37-41", "url": "http://www.unisport.dk/fodboldudstyr/select-fodboldstromper-italia-blahvid/51134/", "free_porto": "0", "price": "59,00", "package": "0", "delivery": "4-8 dage", "kid_adult": "1", "price_old": "69,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/51134_mellem.jpg", "id": "51134", "women": "0"}, {"kids": "0", "name": "Adidas - Spezial Navy/Lysebl\u00e5", "sizes": "EU 36\u2154/UK 4,EU 38/UK 5,EU 38\u2154/UK 5\u00bd,EU 40/UK 6\u00bd,EU 40\u2154/UK 7,EU 41\u2153/UK 7\u00bd,EU 42\u2154/UK 8\u00bd,EU 43\u2153/UK 9,EU 44/UK 9\u00bd,EU 44\u2154/UK 10,EU 46/UK 11,EU 47\u2153/UK 12", "url": "http://www.unisport.dk/fodboldstoevler/adidas-spezial-navylysebla/52041/", "free_porto": "0", "price": "509,00", "package": "0", "delivery": "1-2 dage", "kid_adult": "1", "price_old": "599,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/52041_mellem.jpg", "id": "52041", "women": "0"}, {"kids": "0", "name": "Macron - Spilles\u00e6t Raven Hvid/Sort", "sizes": "Small,Medium", "url": "http://www.unisport.dk/fodboldudstyr/macron-spillesaet-raven-hvidsort/65457/", "free_porto": "0", "price": "199,00", "package": "0", "delivery": "4-8 dage", "kid_adult": "0", "price_old": "349,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/65457_mellem.jpg", "id": "65457", "women": "0"}, {"kids": "0", "name": "Danmark - H\u00f8j Hat", "sizes": "One Size Adult", "url": "http://www.unisport.dk/fodboldtroejer/danmark-hoj-hat/54834/", "free_porto": "0", "price": "49,00", "package": "0", "delivery": "1-2 dage", "kid_adult": "0", "price_old": "0,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/54834_mellem.jpg", "id": "54834", "women": "0"}, {"kids": "0", "name": "Nike - Shorts Woven Dame R\u00f8d", "sizes": "X-Small,Small,Large,X-Large", "url": "http://www.unisport.dk/fodboldudstyr/nike-shorts-woven-dame-rod/57508/", "free_porto": "0", "price": "149,00", "package": "0", "delivery": "5-14 dage", "kid_adult": "0", "price_old": "199,00", "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/57508_mellem.jpg", "id": "57508", "women": "1"}]}')

    products = []

    for jsonProduct in jsonProducts['latest']:
        product = Product()
        product.name = toAscii(jsonProduct['name'])
        product.kids = int(jsonProduct['kids'])
        product.price = toFloatDkInput(jsonProduct['price'])
        product.sizes = toAscii(jsonProduct['sizes'])
        product.url = toAscii(jsonProduct['url'])
        product.free_porto = int(jsonProduct['free_porto'])
        product.package = toAscii(jsonProduct['package'])
        product.delivery = toAscii(jsonProduct['delivery'])
        product.kid_adult = int(jsonProduct['kid_adult'])
        product.price_old = toFloatDkInput(jsonProduct['price_old'])
        product.img_url = toAscii(jsonProduct['img_url'])
        product.id = int(jsonProduct['id'])
        product.women = int(jsonProduct['women'])

        products.append(product)
        
    return products


def loadProductsAndSortByPriceAsc():
    products = loadAllProducts()
    sortedByPriceAsc = sorted(products, key=lambda product: product.price)
    
    return sortedByPriceAsc


def productsSortedByPriceAsc(pageNumber):
    sortedByPriceAsc = loadProductsAndSortByPriceAsc()
    
    return getRangeOfListBaseOnPageNumber(sortedByPriceAsc, pageNumber)


def productsKidsOnlySortedByPriceAsc(pageNumber):
    productsByPrice = loadProductsAndSortByPriceAsc()
    
    productsForKidsOnly = []
    
    for product in productsByPrice:
         if product.kids == 1:
              productsForKidsOnly.append(product)
    
    return getRangeOfListBaseOnPageNumber(productsForKidsOnly, pageNumber)
    

# Get product by id, returns None if no matching product is found
def getProductById(productId):
    allProducts = loadAllProducts()
    for product in allProducts:
         if product.id == productId:
               return product
               
    return None

    
def toFloatDkInput(input):
    return float(input.replace(",", "."))


# Convert input to ascii ignoring all non-ascii chars    
def toAscii(input):
    return input.encode('ascii', errors='ignore')
    

# Returns sublists based on given page number with page size 10
def getRangeOfListBaseOnPageNumber(list, pageNumber):
    pageSize = 10
    
    if pageNumber < 1:
         pageNumber = 1
    
    rangeStart = (pageNumber-1)*pageSize
    
    if rangeStart > len(list):
         return []
    
    rangeEnd = min(len(list), rangeStart + 10)
    
    return list[rangeStart: rangeEnd]
