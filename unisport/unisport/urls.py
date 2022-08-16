from django.contrib import admin
from django.urls import path
from unisport_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.ApiProductListView.as_view(),),
    path('products/<int:id>/', views.ApiProductView.as_view(),),
]
