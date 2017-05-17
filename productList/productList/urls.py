from django.conf.urls import include, url
from django.contrib import admin
from productList import views

urlpatterns = [
    url(r'^products/', include('products.urls'), name='products'),
    url(r'^documentation/$', views.documentation, name='documentation'),
    url(r'^$', views.home, name = 'home'),
]
