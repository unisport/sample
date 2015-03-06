from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

import views


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(
        r'^products/$',
        views.ProductListView.as_view(template_name='product_list.html'),
        name='product_list'
    ),
    url(
        r'^products/kids/$',
        views.ProductListView.as_view(template_name='product_list.html'),
        {'kids': True},
        name='product_list_kids'
    ),
    url(
        r'^products/(?P<pk>\d+)/delete/$',
        views.ProductDeleteView.as_view(template_name='product_delete.html'),
        name='product_delete'
    ),
    url(
        r'^products/(?P<pk>\d+)/update/$',
        views.ProductUpdateView.as_view(template_name='product_update.html'),
        name='product_update'
    ),
    url(
        r'^products/create/$',
        views.ProductCreateView.as_view(template_name='product_create.html'),
        name='product_create'
    ),
    url(
        r'^products/(?P<pk>\d+)$',
        views.ProductDetailView.as_view(template_name='product_detail.html'),
        name='product'
    ),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
