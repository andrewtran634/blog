from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from login.models import User

def index(request, user_id):
	user = get_object_or_404(Question, pk=user_id)
	render(request, 'post/index.html', {'user' : user})
