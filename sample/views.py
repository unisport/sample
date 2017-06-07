from django.shortcuts import render
import json
import urllib.request
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Reads the data from UniSport and makes it usable as a list
urlData  = "http://www.unisport.dk/api/sample/"
webURL   = urllib.request.urlopen(urlData)
data 	 = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
JSON_object = json.loads(data.decode(encoding))["products"]

# Sort the list of products, based on price
product_list = sorted(JSON_object, key=lambda k: float(k["price"].replace(",", ".")))

# Creates a new list, made only of kids products
product_list_kids = [p for p in product_list if p["kids"] == "1"]

def products(request):
	# See https://docs.djangoproject.com/en/1.11/topics/pagination/ for documentation on Pagination
	paginator = Paginator(product_list, 10)

	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
    	# If page is not an integer, deliver first page.
		products = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		products = paginator.page(paginator.num_pages)

	return render(request, 'sample/products.html', {'products': products})

def kids(request):
	# See https://docs.djangoproject.com/en/1.11/topics/pagination/ for documentation on Pagination
	paginator = Paginator(product_list_kids, 10)

	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
    	# If page is not an integer, deliver first page.
		products = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		products = paginator.page(paginator.num_pages)

	return render(request, 'sample/products.html', {'products': products})

def id(request, pid=None):
	product = [p for p in product_list if p["id"] == pid]
	if len(product) != 0:
		# In case PID is invalid, doing this would throw an IndexError
		# Invalid PID is handled in id.html
		product = product[0]

	return render(request, 'sample/id.html', {'product': product})

# Returns the front page
def home(request):
	return render(request, "sample/home.html", {})