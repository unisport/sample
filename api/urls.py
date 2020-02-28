"""Url dispatcher for api app."""
from django.urls import path
from api import views as api_views

urlpatterns = [
    path('products/', api_views.ProductView.as_view()),
    path('products/<id>', api_views.ProductViewDetail.as_view()),
    path('products/<age>/', api_views.ProductViewAge.as_view())
]
