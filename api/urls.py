from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from api import views as api_views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'^products$', api_views.ProductViewSet, basename="products")
router.register(
    r'products/(?P<age>.+)$',
    api_views.ProductGenderViewSet,
    basename="products_gender"
)

urlpatterns = [
    path('api/', include(router.urls))
]
