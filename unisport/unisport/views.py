from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from unisport import models


class ProductView(TemplateView):
    """Single product view page."""

    def get_context_data(self, product_id=None):
        context = super(ProductView, self).get_context_data()

        context.update({
            'product': get_object_or_404(models.Product, fake_id=product_id)
        })

        return context


class ProductListView(TemplateView):
    """Product list view page."""

    items_per_page = 10

    def get_context_data(self):
        context = super(ProductListView, self).get_context_data()

        page = self.request.GET.get('page')
        product_list = models.Product.objects.all().order_by('price')
        paginator = Paginator(product_list, self.items_per_page)
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
