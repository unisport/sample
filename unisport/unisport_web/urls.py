from django.urls import path

from .views import ProductDeleteView, ProductDetailView, ProductListView

urlpatterns = [
    path(r"", ProductListView.as_view(), name="products"),
    path(r"products", ProductListView.as_view(), name="products"),
    path(r"product/<int:pk>", ProductDetailView.as_view(), name="product-detail"),
    path(
        r"product/<int:pk>/delete", ProductDeleteView.as_view(), name="product-delete"
    ),
]
