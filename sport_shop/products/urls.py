from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.listing_products, name='products'),
    url(r'^(?P<product_id>[0-9]+)/$',
        views.detail_product, name='detail_product'),
    url(r'create_product', views.create_product, name='create_product'),
    url(r'delete_product', views.delete_product, name='delete_product'),
]
