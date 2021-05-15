from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('blog/<int:pk>', views.info_blog, name='post_info'),
    path('blog/new',views.post_new, name='post_creation'),
    path('blog/<int:pk>/change', views.blog_change, name='blog_change'),
    path('',include('bloggers.urls'))
]
