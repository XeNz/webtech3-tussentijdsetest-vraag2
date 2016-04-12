from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<firstname>[A-z ]+)/(?P<lastname>[A-z ]+)/$', views.detail, name='detail'),
]
