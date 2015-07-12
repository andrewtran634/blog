from django.conf.urls import url, patterns

from . import views

urlpatterns = [
    url(r'^(?P<user_id>[0-9]+)/$', views.what, name='what'),
    """url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),"""
]