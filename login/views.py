from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import User

def index(request):
	return render(request, 'login/index.html')

def attempt(request, user_name, password):
	return render(request, 'login/yes.html')