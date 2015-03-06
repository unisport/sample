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
        r'^products/(?P<product_id>\d+)$',
        views.ProductView.as_view(template_name='product.html'),
        name='product'
    ),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
