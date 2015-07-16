from django.conf.urls import url, patterns

from . import views

urlpatterns = [
    #url(r'^(?P<user_id>[0-9]+)/$', views.main, name='main'),
    url(r'^$', views.test, name='test'),
    url(r'^(?P<user_id>[0-9]+)/new/$', views.new, name='new'),
    url(r'^(?P<user_id>[0-9]+)/submit/$', views.submit, name='submit'),
    url(r'^(?P<post_id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<post_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<post_id>[0-9]+)/editsubmit/$', views.editsubmit, name='editsubmit'),

]