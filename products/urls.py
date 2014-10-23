from django.conf.urls import patterns, url

__author__ = 'Sergey Smirnov <smirnoffs@gmail.com>'

urlpatterns = patterns('products',
                       url(r'^$', 'views.products', name='catalog'),
                       url(r'^kids/$', 'views.kids', name='kids'),
                       url(r'^(?P<id>\d+)/$', 'views.product'),
                       )

