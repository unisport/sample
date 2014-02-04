from django.http import HttpResponse
from products.models import Get
from django.core.paginator import Paginator
from django.shortcuts import render

# Originally, there was a difference between the category template, and the index template.
# As the code progressed, this difference was eliminated, and now only a single  

def index(request):
	"""	index
		Default view, returns all items
	"""
	model = Get('http://www.unisport.dk/api/sample/')
	data = model.read()
	
	p = Paginator(data['latest'], 10)
	page_number = request.GET.get('page', 1)

	page = p.page(page_number)
	context = {'page': page}
	return render(request, 'products/category.html', context)

def category(request, category):
	""" category
		Takes a string parameter
		Returns only items where (parameter = 1)
		Currently does not handle errors, site does throws error messages.
	"""
	model = Get('http://www.unisport.dk/api/sample/')
	data = model.read()
	data_filtered = [i for i in data['latest'] if i[category] == '1']

	p = Paginator(data_filtered, 10)

	page_number = request.GET.get('page', 1)

	page = p.page(page_number)
	context = {'page': page, 'category': category}
	return render(request, 'products/category.html', context)

def details(request, id):
	""" details
		Takes a integer paramter
		Returns a single item, and all data thereof.
		Current template lists all key, value pars, with no regard for data, privacy or permissions.
		A couple of data points has, as an example, been shown in an more appropriate way.
	"""
	model = Get('http://www.unisport.dk/api/sample/')
	data = model.read()

	# This should have been handled by only extracting the correct data.
	# python dicts are not meant to be traversed.	
	found_object = None
	for object in data['latest']:
		if object['id'] == id:
			found_object = object

	context = {'object': found_object}
	return render(request, 'products/details.html', context)