# Import the URL module and the views from this app.
from django.conf.urls import url
from . import views

# These URL patterns are included after the /products/ rule in the root URL patterns.
# The empty rule is /products/ which will call the views.products function with no other argument than the request object.
# The /(kids)/ rule also calls the views.products function, but because kids is wrapped in parenthesis the function will be called with kids in the functions second argument.
# The /id/ rule will call the function views.product_id again with no other argument than the request object.
# The /id/(\d+)/ will also call the functions views.product_id but the number in the parenthesis will be passed to the functions as its second argument.
urlpatterns = [
	url(r"^$", views.products),
	url(r"^(kids)/$", views.products),
	url("^id/$", views.product_id),
	url(r"^id/(\d+)/$", views.product_id),
]