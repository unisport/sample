#from __future__ import unicode_literals
#from django.shortcuts import render
from django.http import HttpResponse
import urllib, json

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
	
	i = 0
	
	html += "<table>"
	while i < len(l):
		p = l[i]
		html += "<tr>"
		html += "<td><a href=\"/products/id/%s\">%s</a></td>" % (p["id"], p["name"])
		html += "<td align=\"right\">%s</td>" % p["price"]
		html += "<td>%s</td>" % p["currency"]
		html += "</tr>"
		i += 1
	html += "</table>"
	
	page = request.GET.get("page")
	if page != None and page.isdigit():
		html += "<br />Page " + str(page)
	
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