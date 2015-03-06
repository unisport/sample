from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from unisport import models


class ProductView(TemplateView):

    def get_context_data(self, product_id=None):
        context = super(ProductView, self).get_context_data()
        context.update({
            'product': get_object_or_404(models.Product, fake_id=product_id)
        })
        return context
