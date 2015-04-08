from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^products/', include('product_api.urls')),
]
