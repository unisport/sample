from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brands/nike', views.brand_list_nike, name='brand_list_nike'),
    path('brands/adidas', views.brand_list_adidas, name='brand_list_adidas'),
    path('products/', views.product_list, name='products'),
    path('products/outlet', views.product_list_outlet, name='product_list_outlet'),
    path('products/men', views.product_list_men, name='product_list_men'),
    path('products/women', views.product_list_women,
         name='product_list_women'),
    path('products/kids', views.product_list_kids, name='product_list_kids'),
    path('product/<int:pk>', views.product_details, name='product_details'),
    path('import', views.import_data, name='import_data'),
]
