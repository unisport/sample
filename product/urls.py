from django.conf.urls import url
from . import views

# Avoiding hardcode url
app_name = 'product'

urlpatterns = [
    # ~/product/
    url(r'^$', views.ProductView.as_view(), name='product'),

    # ~/product/<product_id>
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),

    # ~/product/kids
    url(r'^kids/', views.KidsView.as_view(), name='kidsView'),

    # ~/product/add/
    url(r'^add/$', views.ProductCreate.as_view(), name='product-add'),

    # ~/product/<product_id>/
    url(r'^(?P<pk>[0-9]+)/update$', views.ProductUpdate.as_view(), name='product-update'),

    # ~/product/<product_id>/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', views.ProductDelete.as_view(), name='product-delete'),
]