from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from products.models import Product


class ProductListView(ListView):
    model = Product
    paginate_by = 10


class ProductDetailView(DetailView):
    model = Product


class DocumentationView(TemplateView):
    template_name = 'products/documentation.html'


class IndexView(TemplateView):
    template_name = 'products/index.html'


class ProductCreateView(SuccessMessageMixin, CreateView):
    model = Product
    fields = ('name', 'price', 'image',)
    success_message = "%(name)s was created successfully"

    def get_success_url(self):
        return reverse('product-detail', kwargs={'pk': self.object.pk})


class ProductUpdateView(SuccessMessageMixin, UpdateView):
    model = Product
    fields = ('name', 'price', 'image',)
    template_name_suffix = '_update_form'
    success_message = "%(name)s was updated successfully"

    def get_success_url(self):
        return reverse('product-detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product-list')
