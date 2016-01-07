from django.shortcuts import get_object_or_404, render, redirect
from django.template import RequestContext, loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import logout, login, authenticate
from django.contrib import *
from .models import User
from .forms import LoginForm, RegForm
from django import forms

def index(request):
	user_list = User.objects.all()
	log = LoginForm()
	reg = RegForm()
	if 'username' in request.session:
		print request.session['username']
	if 'username' not in request.session:
		return render(request, 'login/index.html', {'log' : log, 'reg' : reg}) 
	else:
		username = request.session['username']
		return redirect(reverse('post:main', args=(username,)))

def go(request, user_id):
	u = get_object_or_404(User, pk=user_id)
	#return HttpResponseRedirect(reverse('post:test'))
	return render(request, 'login/attempt.html', {'name' : u.username})
def lattempt(request):
	if request.method == 'POST':
		attempt = LoginForm(data=request.POST)
		#user = authenticate(username=attempt.cleaned_data['username'], password=attempt.cleaned_data['password'])
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user:
			request.session['username'] = request.POST['username']
			auth.login(request, user)
			user.is_active = True
			user.save()
			print 'yaaayy'
			print request.POST['password']

			return redirect(reverse('post:main', args=(user.username,)))
		else:
			messages.error(request, 'No user with those credentials')
			return redirect(reverse('login:index'))

def rattempt(request):
	if request.method == 'POST':
		attempt = RegForm(request.POST)
				#check passwords match
		try:
			taken = User.objects.get(username=request.POST['username'])
			messages.error(request, 'Username taken')
			return redirect(reverse('login:index'))
		except:
			print 'user is unique'


		if request.POST['password'] != request.POST['password2']:
			messages.error(request, 'Passwords did not match')
			return redirect(reverse('login:index'))
		else:
			if attempt.is_valid():
				new_user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
				#new_user = attempt.save()
				#new_user.save()
				#new_user.set_password(new_user.password)
				new_user.save()
				check = auth.authenticate(username=new_user.username, password=request.POST['password'])
				print new_user.username
				print new_user.password
				#if check is not None:
				#	if check.is_active:
				auth.login(request, check)
				request.session['username'] = new_user.username
				return redirect(reverse('post:main', args=(new_user,)))
#def register(request):
def done(request, username):
	u = get_object_or_404(User, username=username)
	auth.logout(request)
	u.is_authenticated = False
	#u.is_active = False
	u.save()
	if 'username' in request.session:
		del request.session['username']
	return redirect(reverse('login:index'))