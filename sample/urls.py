from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^products$', views.products, name='products'),
	url(r'^products/kids', views.kids, name='kids'),
	url(r'^products/id/$', views.id, name='id'),
	url(r'^products/id/(\d+)', views.id, name='id'),
]