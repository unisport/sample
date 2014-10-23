__author__ = 'Sergey Smirnov <smirnoffs@gmail.com>'

from django.conf.urls import patterns, include, url
from django.contrib import admin
from products import urls as products_urls

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^products/', include(products_urls)),
                       url(r'^admin/', include(admin.site.urls)),
)

