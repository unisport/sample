from django.conf.urls import patterns, url
from products import views

urlpatterns = patterns('',
    # Fallback, index
    url(r'^$', views.index, name='index'),
	
	# Example: "sample/kids/" or "sample/women/"
	url(r'^(?P<category>\w+)/$', views.category, name='category'),
	
	# Example: "sample/id/35501"
	url(r'^id/(?P<id>\d+)/$', views.details, name='detail'),
)