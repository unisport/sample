from django.urls import path

from . import views

app_name = 'unisport_app'

urlpatterns = [
    # Index - redirects to products/
    path('', views.index, name='index'),

    # views using API data
    path('products/', views.products, name='products'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),

    # views using data from database
    path('products_db/', views.products_from_db, name='products_from_db'),
    path('products_db/<int:id>/', views.product_from_db_detail,
         name='product_from_db_detail'),
]
