from django.conf.urls import url

# instead of writing 'from . import' i write the app name,
# because it makes the code more readable
from products import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<product_id>[0-9]+)/$', views.product_details, name='detail'),
    url(r'^kids/$', views.IndexView.as_view(), name='kid-section'),
    url(r'^kids/(?P<product_id>[0-9]+)/$', views.kid_details, name='kids'),
]
