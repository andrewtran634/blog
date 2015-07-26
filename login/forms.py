from django import forms
from .models import User
class LoginForm(forms.ModelForm):
		#excludes = ['id', 'email', 'first_name', 'last_name']
	#user_name = forms.CharField(label='username', max_length=20)
	password = forms.CharField(label='password', widget=forms.PasswordInput(attrs=dict(required=True, max_length=20)))
	class Meta:
		model=User
		fields = ['username', 'password']
	"""
	def user_check:
		try:
			test = User.objects.get(user_name.cleaned_data['username'])
		except User.DoesNotExist:
			return False
		return True"""

class RegForm(forms.ModelForm):
		#excludes = ['id', 'email', 'first_name', 'last_name']
	#user_name = forms.CharField(label='username', max_length=20)
	password = forms.CharField(label='password', widget=forms.PasswordInput(attrs=dict(required=True, max_length=20)))
	password2 = forms.CharField(label='password2', widget=forms.PasswordInput(attrs=dict(required=True, max_length=20)))
	class Meta:
		model = User
		fields = ['username', 'password']
	"""
	def name_check:
		try:
			test = User.objects.get(user_name.cleaned_data['username'])
		except User.DoesNotExist:
			return True
		return False
		#raise forms.ValidationError()

	def pass_check:
		if password != password2:
			return False
			#raise forms.ValidationError()"""
			