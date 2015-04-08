from django.conf.urls import url
from product_api import views

urlpatterns = [
    url(r'^$', views.product_list),
    url(r'^kids/$', views.product_kids),
    url(r'^id/(?P<product_id>[0-9]+)/$', views.product_id),
]
