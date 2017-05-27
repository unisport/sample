#from __future__ import unicode_literals
#from django.shortcuts import render
from django.http import HttpResponse
import urllib, json
import pprint

product_list = json.loads(urllib.urlopen("http://www.unisport.dk/api/sample/").read())["products"]
product_list = sorted(product_list, key=lambda k: float(k["price"].replace(",", ".")))
product_list_kids = [p for p in product_list if p["kids"] == "1"]

# Views
def products(request, kids=None):
	
	if kids == None or kids == "":
		l = product_list
		html = header("All products")
		html += "<h1>All products</h1>"
		html += "<p><a href=\"/products/kids/\">Click here to see only kids products</a></p>"
	else:
		l = product_list_kids
		html = header("Kids products")
		html += "<h1>Kids products</h1>"
		html += "<p><a href=\"/products/\">Click here to see all products</a></p>"
	
	items_per_page = 5
	
	page = request.GET.get("page")
	if page == None or not page.isdigit() or int(page) <= 0:
		page = 1
		
	n = (int(page) - 1) * items_per_page
	
	html += "<table>"
	html += "<tr><th></th><th colspan=\"2\">Price</th></tr>"
	i = 0
	while i < items_per_page and n < len(l):
		p = l[n]
		html += "<tr>"
		html += "<td><a href=\"/products/id/%s\">%s</a></td>" % (p["id"], p["name"])
		html += "<td align=\"right\">%s</td>" % p["price"]
		html += "<td>%s</td>" % p["currency"]
		html += "</tr>"
		i += 1
		n += 1
	html += "</table>"
	
	html += "<p><a href=\"?page=%d\">Previous page</a> <a href=\"?page=%d\">Next page</a></p>" % (int(page) - 1, int(page) + 1)
	
	html += footer()
	return HttpResponse(html)

def product_id(request, pid=None):

	if pid == None or pid == "":
		html = header("No product id provided")
		html += "<p>You have not provided a product id</p>"
		html += "<p><a href=\"/products/\">Back to product list</a></p>"
	else:
		product = next((p for p in product_list if p["id"] == pid), None)
		html = header(product["name"])
		html += "<p><a href=\"/products/\">Back to product list</a></p>"
		html += "<h1>%s</h1>" % product["name"]
		html += "<p>" + pprint.pformat(product).replace("\n", "<br />") + "</p>"
	
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