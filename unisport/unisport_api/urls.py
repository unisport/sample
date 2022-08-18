from django.urls import include, re_path
from rest_framework import routers

from .views import CurrencyViewSet, ProductViewSet

api_router = routers.SimpleRouter()
api_router.register(r"currencies", CurrencyViewSet, basename="currency")
api_router.register(r"products", ProductViewSet, basename="product")

urlpatterns = [re_path(r"", include(api_router.urls))]
