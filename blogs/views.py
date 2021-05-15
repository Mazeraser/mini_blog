from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.

def post_new(request):
	form = PostForm()
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.Author = request.user
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
		if form.is_valid():
			post = form.save(commit=False)
			post.Author = request.user
			post.Date = timezone.now()
			post.save()
			return redirect('post_info', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_new.html', {'form': form})
	# нужно сделать ещё так, чтобы показывало кто, когда и как изменил пост

def home(request):
	posts = Post.objects.filter(Date__lte=timezone.now()).order_by('Date')
	return render(request, 'index.html', {'posts': posts})


def info_blog(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/blog_page.html', {'post': post})