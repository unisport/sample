from django.conf.urls import url
from api.views import ProductList

urlpatterns = [
    url(r'^$', ProductList.as_view(), name='product_list')
]
