from django.http import HttpResponse
import urllib, json, math

product_list = json.loads(urllib.urlopen("http://www.unisport.dk/api/sample/").read())["products"]
product_list = sorted(product_list, key=lambda k: float(k["price"].replace(",", ".")))
product_list_kids = [p for p in product_list if p["kids"] == "1"]

# Views
def products(request, kids=None):
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
	
	page = request.GET.get("page")
	if page == None or not page.isdigit() or int(page) < 1:
		page = 1
	else:
		page = int(page)
	
	items_per_page = 10
	n = (page - 1) * items_per_page
	
	html += "<table>"
	html += "<tr><th colspan=\"2\">Product</th><th colspan=\"2\">Price</th><th>Delivery</th></tr>"
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
	
	html += "<p>Page %d of %d<br />" % (page, math.ceil(len(l) / float(items_per_page)))
	if page > 1:
		html += "<a href=\"?page=%d\">Previous page</a> "  % (page - 1)
	if n < len(l):
		html += "<a href=\"?page=%d\">Next page</a>" % (page + 1)
	html += "</p>"
	
	html += footer()
	return HttpResponse(html)

def product_id(request, pid=None):
	product = next((p for p in product_list if p["id"] == pid), None)
	if product == None:
		html = header("Invalid product id")
		html += "<p>You have provided an invalid product id</p>"
		html += "<p><a href=\"/products/\">Back to product list</a></p>"
	else:
		html = header(product["name"])
		html += "<p><a href=\"/products/\">Back to product list</a></p>"
		html += "<h1>%s</h1>" % product["name"]
		html += "<a href=\"%s\" title=\"Click here for larger image\" target=\"_blank\"><img src=\"%s\" /></a>" % (product["img_url"], product["image"])
		html += "<table>"
		html += "<tr><th>Price:</th><td align=\"right\">%s %s</td></tr>" % (product["price"], product["currency"])
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
	
	html += footer()
	return HttpResponse(html)

# HTML Helper functions
def header(title):
	html = "<html><head><title>"
	html += title
	html += "</title></head><body>"
	return html

def footer():
	html = "</body></html>"
	return html