from django.shortcuts import get_object_or_404, render, redirect
from django.template import RequestContext, loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import User

def index(request):
	user_list = User.objects.all()
	return render(request, 'login/index.html', {'user_list' : user_list})
"""
def go(request, user_id):
	u = get_object_or_404(User, pk=user_id)
	return HttpResponseRedirect(reverse(post.views.what, args=u.id))
	#return render(request, 'login/attempt.html', {'name' : u.username})
	#return render(request, '/post/', {})
"""
