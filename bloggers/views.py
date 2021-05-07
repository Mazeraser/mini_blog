from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from blogs.models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import BloggerInfo
from .forms import Registrations

def user(request,username):
	info_user = {
		'user':BloggerInfo.objects.create(name=username),
		'posts':Post.objects.filter(Author=User.objects.filter(username=username)[:1],Date__lte=timezone.now()).order_by('Date')
	}
	return render(request,'blogger_page.html',info_user)
def register(request):
	if request.method == 'POST':
		form = Registrations(request.POST)
		if form.is_valid():
			return HttpResponseRedirect(reverse('registration/register_done.html'))
	else:
		form = Registrations()
		return render(request,'registration/register.html',{'form':form})