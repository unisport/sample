from django.conf.urls import url
from products import views


app_name = 'products'
urlpatterns = [
    url(r'^products/$', views.ProductList.as_view(), name='index'),
    url(r'^products/page=(?P<page>[0-9]+)/$', views.ProductDetail.as_view(), name='paginated'),
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(), name='detail'),
    url(r'^products/kids/$', views.KidsProductList.as_view(), name='kids'),
]
