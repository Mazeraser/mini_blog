from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from blogs.models import Post
from .models import BloggerInfo

def user(request,username):
	info_user = {
		'user':BloggerInfo.objects.create(name=username),
		'posts':Post.objects.filter(Author=User.objects.filter(username=username)[:1],Date__lte=timezone.now()).order_by('Date')
	}
	return render(request,'blogger_page.html',info_user)