from django.conf.urls import include, url
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='products', permanent=False)),
    url(r'^products/', include('product_api.urls')),
]
