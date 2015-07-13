from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from login.models import User
#from login.views import go, 

def what(request, user_id):
	u = get_object_or_404(User, pk=user_id)
	return render(request, 'post/index.html', {'user' : u})

def test(request):
	u = get_object_or_404(User, pk=1)
	return render(request, 'post/index.html', {'user' : u})