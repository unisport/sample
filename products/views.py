#from __future__ import unicode_literals
#from django.shortcuts import render
from django.http import HttpResponse

def products(request, kids=None):
	html = ""
	if kids == None or kids == "":
		html += "<h1>List of products here</h1>"
	else:
		html += "<h1>List of kids products here</h1>"
	page = request.GET.get("page")
	if page != None and page.isdigit():
		html += "<br />Page " + str(page)
	return HttpResponse(html)

def product_id(request, pid=None):
	html = ""
	if pid == None or pid == "":
		html += "Error you have not provided a product id"
	else:
		html += "Product with id: " + str(pid)
	return HttpResponse(html)