from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',
    url(r'^products/$', product_list_ajax, name='product_list_ajax'),
)
