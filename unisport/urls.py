from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views
from product.api import ProductListAPIView, ProductEditAPIView
from product.views import CatalogView, ProductView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url('^api/products/$', ProductListAPIView.as_view()),
    url('^api/products/edit/(?P<pk>[-\w]+)/$', ProductEditAPIView.as_view()),
    url(r'^products/$', CatalogView.as_view(), name='catalog'),
    url(r'^products/kids/$', CatalogView.as_view(), {'kids': True}, name='kids'),
    url(r'^products/(?P<pk>[-\w]+)/$', ProductView.as_view(), name='product')
]
