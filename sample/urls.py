from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'sample.views.index', name='index'),
     url(r'^products/', include('products.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
