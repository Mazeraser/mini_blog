from django.contrib import admin
from django.urls import path,include
from . import views
from .views import user,SignUpView

urlpatterns = [
	path('signup/', views.SignUpView, name='register'),
	path('accounts/',include('django.contrib.auth.urls')),
	path('accounts/<str:username>',views.user,name='blogger_page')
]