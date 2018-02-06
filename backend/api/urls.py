from django.urls import path
from api import views

urlpatterns = [
    path('products/', views.products_view),
    path('products/<int:page>/', views.products_view),
    path('<int:id>/', views.single_product_view),
    path('kids/<int:page>/', views.kids_products_view)
]