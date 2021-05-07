from django import forms

class Registrations(forms.Form):
	name = forms.CharField(max_length=50)
	password = forms.CharField(widget=forms.PasswordInput)
	bio = forms.CharField(max_length=1000)
	email = forms.CharField()
