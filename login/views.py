from django.shortcuts import get_object_or_404, render, redirect
from django.template import RequestContext, loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import logout, login, authenticate
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
def lattempt(request):
	if request.method == 'POST':
		attempt = LoginForm(request.POST)
		if attempt.is_valid():
			user = authenticate(username=attempt.cleaned_data['username'], password=attempt.cleaned_data['password'])
			if user is not None:
				if user.is_active:
					return redirect('post:main', args=(user,))
				else:
					login(request, user)
					user.is_active = True
					return redirect('post:main', args=(user,))
			else:
				redirect(reverse('login:lerror'))
		else:
			#"Not all fields used"
			return redirect('login:lerror')

def rattempt(request):
	if request.method == 'POST':
		attempt = RegForm(request.POST)
				#check passwords match
		if request.POST['password'] != request.POST['password2']:
			return redirect(reverse('login:rerror'))
		else:
			if attempt.is_valid():
			#new_user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
				new_user = attempt.save()
				#new_user.save()
				new_user.set_password(new_user.password)
				new_user.save()
				check = authenticate(username=new_user.username, password=new_user.password)
				if check is not None:
					if check.is_active:
						login(request, check)
				return redirect(reverse('post:main', args=(new_user,)))
		#else:
		#	return redirect(reverse('login:aerror'))
"""
	if request.method == 'POST':
		attempt = RegForm(request.POST)
		if attempt.is_valid():
			test = User.objects.get(user_name.cleaned_data['username'])
			if User.DoesNotExist:
				#check passwords match
				if attempt.cleaned_data['password'] != attempt.cleand_data['password2']:
					return redirect(reverse('login:rerror'))
				else:
					new_user = User(username=attempt.cleand_data['username'],password=attempt.cleand_data['password'])
					new_user.save()
					return redirect(reverse('post:main', args=(new_user,)))
			else:
				return redirect(reverse('login:aerror'))
		else:
			return redirect(reverse('login:aerror'))"""

#def register(request):
def done(request, username):
	u = get_object_or_404(User, username=username)
	auth.logout(request)
	u.is_authenticated = False
	u.is_active = False
	u.save()
	return redirect(reverse('login:index'))

def lerror(request):
	log = LoginForm()
	reg = RegForm()
	return render(request, 'login/lerror.html', {'log' : log, 'reg' : reg})
def rerror(request):
	log = LoginForm()
	reg = RegForm()
	return render(request, 'login/rerror.html', {'log' : log, 'reg' : reg})
def aerror(request):
	log = LoginForm()
	reg = RegForm()
	return render(request, 'login/aerror.html', {'log' : log, 'reg' : reg})



	#return render(request, '/post/', {})
