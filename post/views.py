from django.shortcuts import get_object_or_404, render, redirect
from django.template import RequestContext, loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from login.models import User
from .models import Post
from django.contrib.auth.decorators import login_required

#from login.views import go, 
def leave(request):
	return redirect('login:index')

def main(request, username):
	u = get_object_or_404(User, username=username)
	p = u.post_set.all().order_by('-id')
	#p = p.order_by('date')
	if u.is_authenticated():
		if 'username' in request.session and request.session['username'] == u.username:
			return render(request, 'post/index.html', {'user' : u, 'posts' : p, 'logged' : 'yes'})
		else:
			return render(request, 'post/index.html', {'user' : u, 'posts' : p})
	else :
		return render(request, 'post/index.html', {'user' : u, 'posts' : p})

def test(request):
	u = get_object_or_404(User, pk=1)
	return render(request, 'post/index.html', {'user' : u})

	#return render(request, 'login/index.html')
#@login_required
def new(request, username):
	u = get_object_or_404(User, username=username)
	return render(request, 'post/new.html', {'user' : u})

#@login_required
def submit(request, username):
	u = get_object_or_404(User, username=username)
	new_post = Post(author=u, subject=request.POST['subject'],text=request.POST['body'],date=timezone.now())
	new_post.save()
	return HttpResponseRedirect(reverse('post:main', args=(new_post.author,)))

#@login_required
def editsubmit(request, post_id):
	p = get_object_or_404(Post, pk=post_id)
	p.text=request.POST['body']
	p.date=timezone.now()
	p.save()
	return HttpResponseRedirect(reverse('post:main', args=(p.author,)))

#@login_required
def delete(request, post_id):
	dpost=get_object_or_404(Post, pk=post_id)
	dpost.delete()
	return HttpResponseRedirect(reverse('post:main', args=(dpost.author,)))

#@login_required
def edit(request, post_id):
	p=get_object_or_404(Post, pk=post_id)
	return render(request, 'post/edit.html', {'post' : p})