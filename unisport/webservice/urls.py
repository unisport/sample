from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^products/$', views.top_ten_cheapest),
    url(r'^products/kids/$', views.kids),
    url(r'^products/id/(?P<id>\d+)$', views.choose_product),
    url(r'^pagination/$', views.paginate)
]
