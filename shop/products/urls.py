#-*- encoding: UTF-8 -*-
"""
Propose: Describe url pattern
Author: 'yac'
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.product, name='product'),
    url(r'^(?P<product_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^kids/', views.kids, name='kids'),
    ]
