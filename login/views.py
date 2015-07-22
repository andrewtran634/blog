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
	badlog=''
	badreg=''
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
			if user:
				badlog = "user doesn't exist"
				#return render(request, 'login/index.html', {'badlog' : badlog})
				#return redirect('login:index')
				raise forms.ValidationError(_('what'), code='what')
		else:
			badlog = "Not all fields used"
			return redirect('login:index', badlog)

	if request.method == 'POST':
		attempt = RegForm(request.POST)
		if attempt.is_valid():
			try:
				test = User.objects.get(user_name.cleaned_data['username'])
			except User.DoesNotExist:
				#check passwords match
				if attempt.cleaned_data['password'] != attempt.cleand_data['password2']:
					badreg = "passwords do not match"
					return render(request, 'login/index.html', {'badreg' : badreg})
				else:
					new_user = User(username=attempt.cleand_data['username'],password=attempt.cleand_data['password'])
					new_user.save()
					#return HttpResponseRedirect(reverse('login:register'))

			badreg = "username already taken"
			return render(request, 'login/index.html', {'badreg' : badreg})
		else:
			badreg = "Not all fields used"
			return render(request, 'login/index.html', {'badreg' : badreg})
#def register(request):
def done(request, username):
	u = get_object_or_404(User, username=username)
	auth.logout(request)
	u.is_authenticated = False
	u.save()
	return redirect(reverse('login:index'))



	#return render(request, '/post/', {})
