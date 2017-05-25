from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.products),
	url(r"kids/", views.products_kids),
	url(r"id/", views.product_id),
]