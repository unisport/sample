from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse_lazy

from unisport import models


class ProductDetailView(DetailView):
    model = models.Product


class ProductListView(TemplateView):
    """Product list view page."""


    def get_context_data(self, kids=False):
        context = super(ProductListView, self).get_context_data()

        items_per_page = self.request.GET.get('items', 10)
        page = self.request.GET.get('page')
        product_list = models.Product.objects.all().order_by('price')
        if kids:
            product_list = product_list.filter(kids=True)

        paginator = Paginator(product_list, items_per_page)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context.update({
            'products': products
        })

        return context


class ProductDeleteView(DeleteView):
    model = models.Product
    success_url = reverse_lazy('product_list')
