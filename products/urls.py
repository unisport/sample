from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'import/$', views.import_products, name='import_products'),

    url(r'kids/$', views.product_list, {'kids': 1}, name='kid_product_list'),
    url(r'(?P<pk>[0-9]+)/$', views.product_detail, name='product_detail'),
    url(r'$', views.product_list, name='product_list'),
)
