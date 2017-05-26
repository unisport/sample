from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.products),
	url(r"^(kids)/$", views.products),
	url("^id/$", views.product_id),
	url(r"^id/(\d+)/$", views.product_id),
]