#-*- encoding: UTF-8 -*-
"""
Propose: Describe shop's url pattern
Author: 'yac'
"""

from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView


urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url=reverse_lazy('list'))),
    url(r'^products/', include('products.urls')),
)
