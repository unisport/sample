from django.conf.urls import url

from products.views import kids_products, product_by_id, products

urlpatterns = [
    url(r'^$', products),
    url(r'^kids/$', kids_products),
    url(r'^(?P<product_id>\d+)/$', product_by_id),
]
