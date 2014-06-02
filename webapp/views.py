# Create your views here.

from django.views.generic import *
from django.views.generic.edit import *
from webapp.models import *
from django.template import *
from pprint import pprint



class HomeView(TemplateView):
	"""
	This class returns the home page with no values showing the options of the user
	"""
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)

		context['list'] = Product.objects.all()
		
		return context


class ProductListView(TemplateView):
	"""
	This class returns a list of merchandise with 10 items ordered by price cheapest first
	"""
	template_name = 'productlist.html'

	def get_context_data(self, **kwargs):
		context = super(ProductListView, self).get_context_data(**kwargs)
		try:
			z = int(self.kwargs['pk'])
			a = (z*10)-10
			b = z*10
			context['list'] = Product.objects.order_by('price')[a:b]
		except:
			context['list'] = Product.objects.all().order_by('price')
		return context

class ProductView(TemplateView):
	"""
	This class returns the home page with no values showing the options of the user
	"""
	template_name = 'productpage.html'


	def get_context_data(self, **kwargs):
		context = super(ProductView, self).get_context_data(**kwargs)
		pk = int(self.kwargs['pk'])
		
		context['Product'] = False

		try:
			context['Product'] = Product.objects.get(id=pk)	
		except:
			print "didnt match id"

		try:
			context['Product'] = Product.objects.get(productID=pk)
		except:
			print "didnt match productID"				
		
		return context

class KidsListView(TemplateView):
	"""
	This class returns a list of merchandise with 10 items ordered by price cheapest first
	"""
	template_name = 'productlist.html'

	def get_context_data(self, **kwargs):
		context = super(KidsListView, self).get_context_data(**kwargs)
		
		try:
			z = int(self.kwargs['pk'])
			a = (z*10)-10
			b = z*10

			context['list'] = Product.objects.filter(kids=1).order_by('price')[a:b]
		except:
			context['list'] = Product.objects.filter(kids=1).order_by('price')

		return context
