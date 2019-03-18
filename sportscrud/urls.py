from django.urls import path, include
from rest_framework import routers

from sportscrud import views


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('kids', views.KidsViewSet)

urlpatterns = [
	path('', include(router.urls)),
]
