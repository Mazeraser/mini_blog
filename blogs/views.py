from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post,UserProfile

# Create your views here.


def home(request):
	Users = UserProfile.objects.all()
	posts = Post.objects.filter(Date__lte=timezone.now()).order_by('Date')
	return render(request, 'index.html', {'posts': posts,'Users':Users})


def info_blog(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/blog_page.html', {'post': post})