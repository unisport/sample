from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',
    url(r'^products/$', product_list_ajax, name='product_list_ajax'),
    url(r'^products/kids/$', product_kids_ajax, name='product_kids_ajax'),

    url(r'^products/add/$', product_add_ajax, name='product_add_ajax'),
    url(r'^products/(?P<product_pk>\d+)/$', product_detail_ajax, name='product_detail_ajax'),
    url(r'^products/(?P<product_pk>\d+)/edit/$', product_edit_ajax, name='product_edit_ajax'),
    url(r'^products/(?P<product_pk>\d+)/delete/$', product_delete_ajax, name='product_edit_ajax'),
)
