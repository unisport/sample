from django.conf.urls import url
from unisport.product import views


urlpatterns = [
    url(r'^$', views.get_products, name='get_products'),
    url(r'^kids/$', views.get_kids_product, name='get_kids_product'),
    url(r'^(?P<product_id>\d+)/$', views.get_product_by_id, name='get_product_by_id'),
    ]
