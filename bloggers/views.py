from django.shortcuts import render, get_object_or_404,redirect
from django.views import generic
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User
from blogs.models import Post
from .models import BloggerInfo

from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrForm

def user(request,username):
	info_user = {
		'user':BloggerInfo.objects.create(name=username),
		'posts':Post.objects.filter(Author=User.objects.filter(username=username)[:1],Date__lte=timezone.now()).order_by('Date')
	}
	return render(request,'blogger_page.html',info_user)
def SignUpView(request):
	if request.method == 'POST':
		user_form = RegistrForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			new_user = authenticate(username=user_form.cleaned_data['username'],password=user_form.cleaned_data['password'],)
			login(request, new_user)
			request.session['return_path'] = request.META.get('HTTP_REFERER','/')
			return render(request, 'blogger_page.html', {'new_user':user})
		else:
			return render(request, 'registration/signup.html',{'user_form': user_form})
	else:
		user_form = RegistrForm()
		return render(request, 'registration/signup.html', {'user_form': user_form})