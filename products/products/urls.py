from django.conf.urls import include, url
from django.contrib import admin
from productsapp.views import *

urlpatterns = [
    # Examples:
    url(r'^products/$', ProductsView.as_view(), name='home'),
    url(r'^products/kids/$', ProductsKidsView.as_view(), name='kids'),
    url(r'^products/(?P<id>\d+)/$', ProductsByIdView.as_view(), name='byId'),
]
