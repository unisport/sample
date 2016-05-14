from django.conf.urls import url
from . import views


urlpatterns = [
    
    url(r'^$', 'products.views.products_list', name='products_list'),
    url(r'^kids/$', 'products.views.products_kids', name='products_kids'),
    url(r'^([0-9]+)/$', 'products.views.product_detail', name='product_detail'),
    
]