from django.shortcuts import render, get_object_or_404,redirect,Http404
from django.utils import timezone
from .models import Post,Comm
from .forms import PostForm,Comment
from django.contrib.auth.models import User

# Create your views here.

def post_new(request):
	form = PostForm()
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.Author = request.User
			post.Date = timezone.now()
			post.save()
			return redirect('post_info', pk=post.pk)
		else:
			form = PostForm()
			return render(request, 'blog/post_new.html', {'form':form})
	else:
		form = PostForm()
		return render(request, 'blog/post_new.html', {'form':form})

def blog_change(request,pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if post.Author != request.user:
			return redirect('Home')
		else:
			if form.is_valid():
				post_ch = form.save(commit=False)
				post_ch.Author = request.user
				post_ch.Date = timezone.now()
				post_ch.save()
				return redirect('post_info', pk=post_ch.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_new.html', {'form': form})

def home(request):
	posts = Post.objects.filter(Date__lte=timezone.now()).order_by('Date')
	return render(request, 'index.html', {'posts': posts})


def info_blog(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
    	form = Comment(request.POST)
    	if form.is_valid():
    		comm = form.save(commit=False)
    		comm.creator = request.user
    		comm.date = timezone.now()
    		comm.post = post.Title
    		comm.save()
    		return redirect('post_info', pk=post.pk)
    else:
    	form = Comment() 
    comments = Comm.objects.filter(post=post.Title)
    return render(request, 'blog/blog_page.html', {'post': post,'comm_form' : form,'comments':comments})