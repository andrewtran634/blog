from django.shortcuts import get_object_or_404, render, redirect
from django.template import RequestContext, loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import logout
from django.contrib import auth
from .models import User
from .forms import LoginForm, RegForm
from django import forms

def index(request):
	user_list = User.objects.all()
	log = LoginForm()
	reg = RegForm()
	return render(request, 'login/index.html', {'log' : log, 'reg' : reg}) 

def go(request, user_id):
	u = get_object_or_404(User, pk=user_id)
	#return HttpResponseRedirect(reverse('post:test'))
	return render(request, 'login/attempt.html', {'name' : u.username})
def attempt(request):
	if request.method == 'GET':
		attempt = LoginForm(request.GET)
		if attempt.is_valid():
			user = authenticate(username=attempt.cleaned_data['username'], password=attempt.cleaned_data['password'])
			if not user:
				redirect(reverse('login:lerror'))
		else:
			#"Not all fields used"
			return redirect('login:lerror')

	if request.method == 'POST':
		attempt = RegForm(request.POST)
		if attempt.is_valid():
			try:
				test = User.objects.get(user_name.cleaned_data['username'])
			except User.DoesNotExist:
				#check passwords match
				if attempt.cleaned_data['password'] != attempt.cleand_data['password2']:
					return redirect(reverse('login:rerror'))
				else:
					new_user = User(username=attempt.cleand_data['username'],password=attempt.cleand_data['password'])
					new_user.save()
					return redirect(reverse('post:main', args=(new_user,)))
			return redirect(reverse('login:aerror'))
		else:
			return redirect(reverse('login:aerror'))
#def register(request):
def done(request, username):
	u = get_object_or_404(User, username=username)
	auth.logout(request)
	u.is_authenticated = False
	u.save()
	return redirect(reverse('login:index'))

def lerror(request):
	render(request, 'login/lerror.html')



	#return render(request, '/post/', {})
