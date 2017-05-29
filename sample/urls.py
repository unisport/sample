from django.conf.urls import include, url
from django.views.generic.base import RedirectView

urlpatterns = [
	url(r"^products/", include("products.urls")),
	url(r"^$", RedirectView.as_view(url="products/", permanent=False)),
]
