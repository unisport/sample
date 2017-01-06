from django.conf.urls import url
from views import LoadDataView, CheapestProductsView, \
    KidsCheapestProductsView, ProductView


urlpatterns = [
    url(r'^$', CheapestProductsView.as_view(), name='cheapest_10'),
    url(r'^(?P<pk>\d+)/$', ProductView.as_view(), name='product'),
    url(r'^kids/$', KidsCheapestProductsView.as_view(), name='kids_products'),
    url(r'^load-data/$', LoadDataView.as_view(), name='load_data'),
]
