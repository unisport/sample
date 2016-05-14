from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

##
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ProductModelForm
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


def product_detail(request, pk):
	try:
		product = Product.objects.get(id=pk)
	except:
		return HttpResponseRedirect(reverse('products_list'))

	return render(request, 'product_detail.html', {"product":product})

#Class Based Views for manipulating information in DB

class CreateProduct(CreateView):
	form_class = ProductModelForm
	template_name = 'create_product.html'
	
	def form_valid(self, form):
		Product.objects.create(**form.cleaned_data)
		return HttpResponseRedirect(reverse('products_list'))

class UpdateProduct(UpdateView):
	model = Product
	success_url='/products/'
	form_class = ProductModelForm
	template_name = 'update_product.html'

	

	# # def post(self, request, *args, **kwargs):
	# # 	return super(UpdateProduct, self).post(request, *args, **kwargs)

class DeleteProduct(DeleteView):
	model = Product
	template_name = 'confirm_delete_product.html'
	success_url='/products/'

	# def get_success_url(self):
	# 	return reverse('product_detail', args(self.request.POST.get('id')))