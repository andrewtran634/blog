from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/go/$', views.go, name='go'),
    url(r'^attempt/$', views.attempt, name='attempt'),
    url(r'^(?P<username>[\w-]+)/done/$', views.done, name='done')
]