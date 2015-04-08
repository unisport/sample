from django.conf.urls import url
from product_api import views

urlpatterns = [
    url(r'^$', views.ProductList.as_view(), name='product-list'),
    url(r'^kids/$', views.product_kids, name='product-kids'),
    url(r'^id/(?P<product_id>[0-9]+)/$', views.product_id, name='product-id'),
]
