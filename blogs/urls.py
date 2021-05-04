from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('blog/<int:pk>', views.info_blog, name='post_info'),
    path('',include('bloggers.urls'))
]
