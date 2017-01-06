__author__ = 'azhukov'

from django.conf.urls import patterns,  url

import views

urlpatterns = patterns(
    '',
    url(r'products/$', views.ItemList.as_view(), name='products'),
    url(r'products/kids/$', views.ItemListKids.as_view(), name='products_kids'),
    url(r'products/(?P<id>[0-9]+)/$', views.ItemSingle.as_view(), name='item_single'),

)

