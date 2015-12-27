from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.listing_products, name='products'),
    url(r'create_product', views.create_product, name='create_product'),
    url(r'delete_product', views.delete_product, name='delete_product'),
]
