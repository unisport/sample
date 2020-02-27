from django.urls import path, include
from rest_framework import routers
from api import views as api_views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'products', api_views.ProductViewSet, basename="products")

urlpatterns = [
    path('api/', include((router.urls, 'api'), namespace="api"))
]
