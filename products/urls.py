from django.conf.urls import patterns, url

import views


urlpatterns = patterns(
    '',
    url(r'import/$', views.import_products, name='import_products'),
)