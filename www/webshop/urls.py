from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='products'),
    path('import', views.import_data, name='import_data'),
]