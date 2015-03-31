# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals

import json

from django.shortcuts import render
from django.views.generic import View

from utils.mixin import JSONResponseMixin
from apps.products.models import Product, Size

__all__ = ('ProductViewHandler', )


class ProductViewHandler(JSONResponseMixin, View):
    ITEM_PER_PAGE = 10

    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        if product_id:
            try:
                product = Product.objects.get(id=product_id)
                self.context['data'] = self._get_product_json(product)
            except (Product.DoesNotExist, IndexError, ValueError) as err:
                self.context['errors'] = 'Product with given id does\'t exist'
                self.context['status'] = False
        else:
            page = request.GET.get('page', '1')
            if page.isdigit():
                page = int(page)
            else:
                page = 1
            products, next_page = self._get_products_list(page, **kwargs)

            self.context['data'] = [self._get_product_json(_) for _ in products]
            if next_page:
                self.context['next'] = '{path}?page={page}'.format(**{
                    'page': next_page,
                    'path': self.request.path
                })

        return self.render_to_response(self.context)

    @staticmethod
    def _get_products_list(page, **kwargs):
        products_count = Product.objects.filter(**kwargs).count()
        start = (page-1)*ProductViewHandler.ITEM_PER_PAGE
        end = page*ProductViewHandler.ITEM_PER_PAGE
        products = Product.objects.filter(**kwargs)[start:end]

        return products, page + 1 if end < products_count else None

    @staticmethod
    def _get_product_json(product):
        return {
            'id': product.id,
            'name': product.name,
            'kids': product.kids,
            'women': product.women,
            'kid_adult': product.kid_adult,
            'package': product.package,
            'free_porto': product.free_porto,
            'delivery': product.delivery,
            'sizes': ', '.join(product.sizes.all().values_list('size', flat=True)),
            'price': product.price,
            'price_old': product.price_old,
            'url': product.url,
            'img_url': product.img_url,
        }