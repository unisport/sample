from django.conf.urls import url, include
from .views import ListProducts, ListKidsProducts, GetProduct

urlpatterns = [
    url(r'^$', ListProducts.as_view(), name='get_products'),
    url(r'^(?P<product_id>\d+)/$', GetProduct.as_view(), name='get_product'),
    url(r'^kids/$', ListKidsProducts.as_view(), name='get_kids_products'),
]