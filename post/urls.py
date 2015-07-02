from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns(
    url(r'^(?P<user_id>[0-9]+)/$', views.index, name='index'),
    """url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),"""
)