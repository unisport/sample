from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'unisport.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/$', 'products.views.paginate'),
    url(r'^products/kids/$', 'products.views.kids'),
    url(r'^products/(?P<page>\d+)$', 'products.views.paginate'),
    url(r'^products/(?P<id>\d+)/$', 'products.views.getitem'))
)
