from rest_framework.routers import DefaultRouter
from . import viewsets

app_name = "main"
router = DefaultRouter()
router.register(r"products", viewsets.ProductsViewSet, "products")
urlpatterns = router.urls 