# We import the HttpResponse class so that the views can return HTML when called.
from django.http import HttpResponse

# The urllib and json modules are imported so the JSON data from the website can be loaded into a variable and we import the math module to allow access to math functions.
import urllib, json, math

# The list of products are saved to a variable by requesting the JSON data from the url and passing it to the json.loads function
# and then we specify that we only want the products property from the json data.
product_list = json.loads(urllib.urlopen("http://www.unisport.dk/api/sample/").read())["products"]

# The product list then sorted using the price as a key, but first we specify that when comparing the keys they must first be converting
# to floats and before we can convert them to floats we need to replace all commas with periods.
product_list = sorted(product_list, key=lambda k: float(k["price"].replace(",", ".")))

# We make a list of all the kids products by copying all items from the product list where the property kids is equal to the string "1"
product_list_kids = [p for p in product_list if p["kids"] == "1"]

# Views
# The products function is the view that will be called if a client requests the URL /products/ or /products/kids/.
# The functions has the required argument request which is always passed by the URL dispatcher and optional argument kids
# which is only passed by the URL dispatcher if the client request /products/kids/.
def products(request, kids=None):

	# In this if else statement we set the list that is to be used.
	# If the kids argument is None or empty then we will use the list of all products else we will use the list of kids products.
	# We also call the header function with an appropriate title based on context, all products or kids products, and save its return value to a html variable.
	# We also add a heading with the same text as the title and a link, to either kids products or all products depending on context, to the html variable.
	if kids == None or kids == "":
		l = product_list
		html = header("All products")
		html += "<h1>All products</h1>"
		html += "<p><a href=\"/products/kids/\">Click here to only see kids products</a></p>"
	else:
		l = product_list_kids
		html = header("Kids products")
		html += "<h1>Kids products</h1>"
		html += "<p><a href=\"/products/\">Click here to see all products</a></p>"
	
	# In the page variable we get the value of the page parameter from the url.
	# After that we check that if the page variable is None or not a digit or less than 1 then it is set set to 1 else the page variable is converted to an int.
	page = request.GET.get("page")
	if page == None or not page.isdigit() or int(page) < 1:
		page = 1
	else:
		page = int(page)
	
	# In the items_per_page varible we specify how many items to show per page. This variable could be moved to the settings file.
	items_per_page = 10
	
	# In the n variable we calculate the index of the first item on the page.
	# So on the first page the first index is 0 and on the seond page the first index is 10 (if we want to show 10 items per page).
	n = (page - 1) * items_per_page
	
	# To show the list of products we use a html table which is added to the html variable.
	html += "<table>"
	html += "<tr><th colspan=\"2\">Product</th><th colspan=\"2\">Price</th><th>Delivery</th></tr>"
	
	# The list is looped through items_per_page times or untill the end of the list is reached.
	# Each loop adds a product from the list as a row the table and after the loop the table is closed.
	i = 0
	while i < items_per_page and n < len(l):
		p = l[n]
		html += "<tr>"
		html += "<td><a href=\"%s\" title=\"Click here for larger image\" target=\"_blank\"><img src=\"%s\" width=\"100px\" /></a></td>" % (p["img_url"], p["image"])
		html += "<td><a href=\"/products/id/%s\">%s</a></td>" % (p["id"], p["name"])
		html += "<td align=\"right\">%s</td>" % p["price"]
		html += "<td>%s</td>" % p["currency"]
		html += "<td>%s</td>" % p["delivery"]
		html += "</tr>"
		i += 1
		n += 1
	html += "</table>"
	
	# After the table a "Page # of #" is shown where the total number of pages is calculated by dividing the length of the list with items_per_page and rounding up.
	html += "<p>Page %d of %d<br />" % (page, math.ceil(len(l) / float(items_per_page)))
	
	# And if we are on a page higher than 1 then a Previous page link is shown that links to the current page number - 1.
	if page > 1:
		html += "<a href=\"?page=%d\">Previous page</a> " % (page - 1)
	
	# And if the n variables is less than the length of list that means that there are more pages so we can show a link to the current page number + 1
	if n < len(l):
		html += "<a href=\"?page=%d\">Next page</a>" % (page + 1)
	html += "</p>"
	
	# In the end we append the output of the footer function to the html variable and then we return the html inside of a HttpResponse.
	html += footer()
	return HttpResponse(html)

# The product_id function is the view that is called when the client requests /products/id/ with or without some number at the end.
# If a number is part of URL it is then passed to the second argument of the function.
# The function returns a HttpResponse with html that shows information about a specific product (if a correct id number is provided) or an error message.
def product_id(request, pid=None):

	# The specific product is found from the list by using the next function to find the product with the provided id.
	# If there is no product in the list with the given id then product is set to None.
	product = next((p for p in product_list if p["id"] == pid), None)
	
	# If the product variable is None then a error message is built detailing that the provided id is invalid.
	if product == None:
		html = header("Invalid product id")
		html += "<p>You have provided an invalid product id</p>"
		html += "<p><a href=\"/products/\">Back to product list</a></p>"
		
	# But if the product variable is not None then we build a html table and fill it with data about the product from the JSON object.
	else:
		html = header(product["name"])
		html += "<p><a href=\"/products/\">Back to product list</a></p>"
		html += "<h1>%s</h1>" % product["name"]
		html += "<a href=\"%s\" title=\"Click here for larger image\" target=\"_blank\"><img src=\"%s\" /></a>" % (product["img_url"], product["image"])
		html += "<table>"
		html += "<tr><th>Price:</th><td align=\"right\">%s %s</td></tr>" % (product["price"], product["currency"])
		
		# If the product has a price_old property that is not empty and if the price property is less than the price_old property
		# then we show the old price with a strike through it.
		if product["price_old"] != "" and product["price"] < product["price_old"]:
			html += "<tr><th>Old price:</th><td align=\"right\"><s>%s %s</s></td></tr>" % (product["price_old"], product["currency"])
			
		html += "<tr><th>Delivery:</th><td>%s</td></tr>" % product["delivery"]
		html += "<tr><th>Free porto:</th><td>%s</td></tr>" % ("Yes" if product["free_porto"] == "1" else "No")
		html += "<tr><th>Sizes:</th><td>%s</td></tr>" % product["sizes"].replace(", ", ",<br />")
		html += "<tr><th>Adult and kid sized:</th><td>%s</td></tr>" % ("Yes" if product["kid_adult"] == "1" else "No")
		html += "<tr><th>Kid sized:</th><td>%s</td></tr>" % ("Yes" if product["kids"] == "1" else "No")
		html += "<tr><th>Women sized:</th><td>%s</td></tr>" % ("Yes" if product["women"] == "1" else "No")
		html += "<tr><th>Customizable:</th><td>%s</td></tr>" % ("Yes" if product["is_customizable"] == "1" else "No")
		html += "</table>"
	
	# In the end of the function we append the output of the footer function and return the html through a HttpResponse.
	html += footer()
	return HttpResponse(html)

# HTML Helper functions
# The header function generates the first part of a basic html document with a title that is passed to the function.
def header(title):
	html = "<html><head><title>"
	html += title
	html += "</title></head><body>"
	return html

# The footer function generates the last part a basic html document.
def footer():
	html = "</body></html>"
	return html