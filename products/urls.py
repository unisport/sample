from django.conf.urls import url, include
from .views import (ListProducts,
	ListKidsProducts, GetProduct,
	CreateProduct, UpdateProduct)

urlpatterns = [
    url(r'^$', ListProducts.as_view(), name='get_products'),
    url(r'^create/$', CreateProduct.as_view(), name='create_product'),
    url(r'^(?P<product_id>\d+)/$', GetProduct.as_view(), name='get_product'),
    url(r'^(?P<product_id>\d+)/update/$', UpdateProduct.as_view(), name='update_product'),
    url(r'^kids/$', ListKidsProducts.as_view(), name='get_kids_products'),
]