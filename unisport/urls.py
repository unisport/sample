from django.urls import path, include

from .views import index

urlpatterns = [
    path('', index),
    path('', include('api.urls', namespace='api'))
]
