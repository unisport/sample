# Import the URL modules and RedirectView so we can redirect from the root to /products/
from django.conf.urls import include, url
from django.views.generic.base import RedirectView

# The list of URL patterns at the root level.
# Having products after the root will include the URL patterns described in products/urls.py
# Since there is no view for the root we make a rule that redirects all requests to the root to /products/ instead.
urlpatterns = [
	url(r"^products/", include("products.urls")),
	url(r"^$", RedirectView.as_view(url="products/", permanent=False)),
]
