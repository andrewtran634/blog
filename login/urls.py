from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/go/$', views.go, name='go'),
    url(r'^lattempt/$', views.lattempt, name='lattempt'),
    url(r'^rattempt/$', views.rattempt, name='rattempt'),
    url(r'^error1/$', views.lerror, name='lerror'),
    url(r'^error2/$', views.aerror, name='aerror'),
    url(r'^error3/$', views.rerror, name='rerror'),
    url(r'^(?P<username>[\w-]+)done/$', views.done, name='done')
]