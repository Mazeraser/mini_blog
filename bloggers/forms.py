from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
 
class RegistrForm(forms.ModelForm):
	email = forms.EmailField(max_length=254)
	bio = forms.CharField(max_length=1000)
	class Meta:
		model = User
		fields = ('username','password', 'email', 'bio')
	def __init__(self, *args, **kwargs):
		super(RegistrForm, self).__init__(*args, **kwargs)
		self.fields['username'].help_text = ''
		self.fields['password'].help_text = ''
