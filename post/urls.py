from django.conf.urls import url, patterns

from . import views

urlpatterns = [
    #url(r'^(?P<user_id>[0-9]+)/$', views.main, name='main'),
    url(r'^$', views.test, name='test'),
    url(r'^new/$', views.new, name='new'),
    url(r'^submit/$', views.submit, name='submit'),
    """url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),"""
]