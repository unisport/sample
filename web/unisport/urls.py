from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from products import views

router = routers.DefaultRouter()
# Map /products/kids/ url
router.register(r'^products/kids', views.KidsProductViewSet)
# Map /products/ and products/:id urls
router.register(r'^products', views.ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include(router.urls)),
]
