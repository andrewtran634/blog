from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from login.models import User
#from login.views import go, 

def main(request, user_id):
	u = get_object_or_404(User, pk=user_id)
	return render(request, 'post/index.html', {'user' : u})

def test(request):
	u = get_object_or_404(User, pk=1)
	return render(request, 'post/index.html', {'user' : u})
	#return render(request, 'login/index.html')

def new(request, user_id):
	u = get_object_or_404(User, pk=user_id)
	return render(request, 'post/new.html', {'user' : u})

def submit(request, user_id):
	u = get_object_or_404(User, pk=user_id)
	new_post = Post(username=u.username, subject=request.POST['subject'],text=request.POST['body'])
	return render(request, 'post/index.html', {'user' : u})