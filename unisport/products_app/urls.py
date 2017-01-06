from rest_framework import routers
from django.conf.urls import url
from . views import ProductViewSet

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)

urlpatterns = router.urls