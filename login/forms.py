from django import forms

class LoginForm(forms.Form):
	user_name = forms.CharField(label='username', max_length=20)
	password = forms.Charfield(label='password', widget=forms.PaswordInput(attrs=dict(required=True, max_length=20)))

class RegForm(forms.Form):
	user_name = forms.CharField(label='username', max_length=20)
	password = forms.Charfield(label='password', widget=forms.PaswordInput(attrs=dict(required=True, max_length=20)))
	password2 = forms.Charfield(label='password2', widget=forms.PaswordInput(attrs=dict(required=True, max_length=20)))

	def name_check:
		try:
			test = User.objects.get(user_name.cleaned_data['username'])
		except User.DoesNotExist:
			#am i supposed to put something here?
		raise forms.ValidationError()

	def pass_check:
		if password != password2:
			raise forms.ValidationError()
		