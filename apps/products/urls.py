# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals

from django.conf.urls import patterns, url

from apps.products.views import ProductViewHandler


urlpatterns = patterns(
    'apps.products',
    url('^$', ProductViewHandler.as_view(), name='products'),
    url('^(?P<product_id>\d+)/$', ProductViewHandler.as_view(), name='product'),
    url('kids/$', ProductViewHandler.as_view(), {'kids': 1}, name='kids_products'),
)