from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Product

#---------------------------------------------------------------------------------------#
#                                                                                       #
#                                   VIEWS PRODUCTS                                      #
#                                                                                       #
#---------------------------------------------------------------------------------------#

# Main page: product
class ProductView(generic.ListView):
    # Overwrite the object_list
    context_object_name = 'all_products'
    template_name = 'product/index.html'
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.order_by('price')


# Kids page
class KidsView(generic.ListView):
    # Overwrite the object_list
    context_object_name = 'kids_products'
    template_name = 'product/kids.html'

    def get_queryset(self):
        return Product.objects.filter(kids='1').order_by('price')


# Detail view of each product
class DetailView(generic.DetailView):
    model = Product
    template_name = 'product/detail.html'


#---------------------------------------------------------------------------------------#
#                                                                                       #
#                                   PRODUCTS HANDLING                                   #
#                                                                                       #
#---------------------------------------------------------------------------------------#


#Create view
class ProductCreate(CreateView):
    model = Product
    fields = ['name',
              'price',
              'price_old',
              'currency',
              'is_customizable',
              'delivery',
              'size',
              'kids',
              'kid_adult',
              'free_porto',
              'image',
              'package',
              'url',
              'online',
              'img_url',
              'women']


#Update view
class ProductUpdate(UpdateView):
    model = Product
    fields = ['name',
              'price',
              'price_old',
              'currency',
              'is_customizable',
              'delivery',
              'size',
              'kids',
              'kid_adult',
              'free_porto',
              'image',
              'package',
              'url',
              'online',
              'img_url',
              'women']


#Delete view
class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product:product')








