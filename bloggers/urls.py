from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path('register/', views.register, name='register'),
	path('accounts/',include('django.contrib.auth.urls')),
	path('accounts/<str:username>',views.user,name='blogger_page')
]