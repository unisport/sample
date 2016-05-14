from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Product

def products_list(request):
	products = Product.objects.all().order_by("price")


	paginator = Paginator(products, 5)
	page = request.GET.get('page')

	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	return render(request, 'products_list.html', {"products":products})

def products_kids(request):
	products_kids = Product.objects.all().filter(kids=1).order_by("price")

	return render(request, "products_kids.html", {"products_kids":products_kids})


def product_detail(request, id):
	try:
		product = Product.objects.get(id=id)
	except:
		return HttpResponseRedirect(reverse('products_list'))

	return render(request, 'product_detail.html', {"product":product})
