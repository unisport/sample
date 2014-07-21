from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('^products/', include('product.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
