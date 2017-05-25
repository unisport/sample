from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^(kids)?/?$", views.products),
	url(r"^id/(\d*)/?$", views.product_id),
]