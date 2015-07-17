from django.shortcuts import get_object_or_404, render, redirect
from django.template import RequestContext, loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from login.models import User
from .models import Post
#from login.views import go, 
def leave(request):
	return redirect('login:index')

def main(request, username):
	u = get_object_or_404(User, username=username)
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
	new_post = Post(author=u, subject=request.POST['subject'],text=request.POST['body'],date=timezone.now())
	new_post.save()
	return HttpResponseRedirect(reverse('post:test'))

def editsubmit(request, post_id):
	p = get_object_or_404(Post, pk=post_id)
	p.text=request.POST['body']
	p.date=timezone.now()
	p.save()
	return HttpResponseRedirect(reverse('post:main'))

def delete(request, post_id):
	dpost=get_object_or_404(Post, pk=post_id)
	dpost.delete()
	return HttpResponseRedirect(reverse('post:test'))

def edit(request, post_id):
	p=get_object_or_404(Post, pk=post_id)
	return render(request, 'post/edit.html', {'post' : p})