from django.conf.urls import url
from api.views import ProductList, ProductKids, ProductDetail

urlpatterns = [
    url(r'^$', ProductList.as_view(), name='product_list'),
    url(r'^kids/$', ProductKids.as_view(), name='product_kids'),
    url(r'^(?P<pk>\d+)/$', ProductDetail.as_view(), name='product_detail'),
]
