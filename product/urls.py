from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url('^kids/$', 'product.views.kids'),
    url('^(?P<id>\d+)/$', 'product.views.single_product'),
    url('^$', 'product.views.products'),
)
