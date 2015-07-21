from django.conf.urls import url, patterns

from . import views

urlpatterns = [
    url(r'^$', views.leave, name='leave'),
    url(r'^(?P<username>[\w-]+)/$', views.main, name='main'),
    url(r'^(?P<username>[\w-]+)/new/$', views.new, name='new'),
    url(r'^(?P<username>[\w-]+)/submit/$', views.submit, name='submit'),
    url(r'^(?P<post_id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<post_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<post_id>[0-9]+)/editsubmit/$', views.editsubmit, name='editsubmit'),

]