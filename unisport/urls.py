from django.contrib import admin
from django.urls import include, path

from products.views import DocumentationView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('documentation/', DocumentationView.as_view(), name="documentation"),
    path('products/', include('products.urls')),
    path('admin/', admin.site.urls),
]
