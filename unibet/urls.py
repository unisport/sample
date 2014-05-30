from django.conf.urls import patterns, include, url
from webapp.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'unibet.views.home', name='home'),
    # url(r'^unibet/', include('unibet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
   	#url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', HomeView.as_view(), name="root"),
    url(r'^products/$', ProductListView.as_view(), name="productlistnoargument"),
    url(r'^products/(?P<pk>\d+)/$', ProductListView.as_view(), name="productlist"),
    url(r'^products/id/(?P<pk>\d+)/$', ProductView.as_view(), name="id"),
    url(r'^products/kids/$', KidsListView.as_view(), name="kidslistnoargument"),
    url(r'^products/kids/(?P<pk>\d+)/$', KidsListView.as_view(), name="kidslist"),
)
