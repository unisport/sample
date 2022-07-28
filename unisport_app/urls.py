from django.urls import path

from . import views

app_name = 'unisport_app'

urlpatterns = [
    path('products/', views.products, name='products'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
]
