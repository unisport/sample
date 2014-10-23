from django.conf.urls import patterns, url

__author__ = 'Sergey Smirnov <smirnoffs@gmail.com>'

urlpatterns = patterns('products',
                       url(r'^$', 'views.products'),
                       url(r'^kids/$', 'views.kids'),
                       url(r'^(?P<id>\d+)/$', 'views.product'),
                       url(r'import_data/$', 'views.import_data', name='import_data'),
                       )

