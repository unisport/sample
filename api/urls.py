from django.conf.urls import url
from api.views import ProductList, ProductKids

urlpatterns = [
    url(r'^$', ProductList.as_view(), name='product_list'),
    url(r'^kids/$', ProductKids.as_view(), name='product_kids'),
]
