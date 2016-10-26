# returns 0 for products and product paging, i.e. /products/ and /products/?page=XX
# returns 1 for kids, i.e. /products/kids/
# returns 2 for single product (i.e. /products/XXXX/) or when nothing else matches
def getMode(requestUri):
    requestUri = normalizeRequestUri(requestUri)
        
    if "/kids/" in requestUri:
        return 1
        
    if requestUri.endswith("/products/") or "?page=" in requestUri:    
        return 0
        
    return 2

    
# Should be called after the correct mode has been determined
# If no page number is given, 1 is returned
def getPageNumber(requestUri):
	pageNumber = "?page=";
	indexOfPageNumber = requestUri.rfind(pageNumber)
	if indexOfPageNumber != -1:
         return int(requestUri[indexOfPageNumber + len(pageNumber):])

	return 1

     
# Should be called after the correct mode has been determined
# Will fail if no (correct) number is present
def getProductId(requestUri):
	requestUri = normalizeRequestUri(requestUri).rstrip("/")
	indexOfLastSlash = requestUri.rfind("/")
	
	return int(requestUri[indexOfLastSlash + 1:])
    
    
def normalizeRequestUri(requestUri):
    if not requestUri.endswith("/"):
        requestUri += "/"
    
    return requestUri
