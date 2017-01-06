from django.conf.urls import url
from django.contrib import admin
from products import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^products/kids', views.products_kids, name='products_kids'),
    url(r'^products/(?P<prod_id>\d+)', views.product_id, name='product_id'),
    url(r'^products/', views.products, name='products'),
]
