from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)

app_name = 'api'
urlpatterns = [
    path('products/kids/', ProductViewSet.as_view({'get': 'list'})),
    path('', include(router.urls)),
]
