# -*- coding: utf-8 -*- #
"""
    product urls
"""
from django.conf.urls import url, patterns

urlpatterns = patterns('products',
                       url(r'^$', 'views.products', name='products'),
                       url(r'^kids/$', 'views.kids', name='kids'),
                       url(r'^(?P<id>[0-9]+)/$', 'views.product', name='product'),
                       )

