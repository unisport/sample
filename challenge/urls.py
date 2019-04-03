from django.urls import path

from . import views

#URLs for the project, shows the URL and the view its using.

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/kids/', views.kids, name='kids'),
    path('products/<int:product_id>/', views.id, name='id'),
    path('products/paging/', views.paging, name='paging'),
]