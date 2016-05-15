from django.conf.urls import url
from . import views

from .views import CreateProduct, UpdateProduct, DeleteProduct

urlpatterns = [
    
    url(r'^$', 'products.views.products_list', name='products_list'),
    url(r'^kids/$', 'products.views.products_kids', name='products_kids'),
    url(r'^(?P<pk>\d+)/$', 'products.views.product_detail', name='product_detail'),
    
    #urls for manipulating data 
    url(r'^update-product/(?P<pk>\d+)$', UpdateProduct.as_view(), name='update_product'),
    url(r'^create-product/$', CreateProduct.as_view(), name='create_product'),
    url(r'^delete-product/(?P<pk>\d+)$', DeleteProduct.as_view(), name='delete_product'),
]
