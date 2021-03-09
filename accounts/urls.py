from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views

from django.contrib.auth.views import auth_logout

urlpatterns =[
		path('api/auth', include('knox.urls')),
		path('api/auth/register', RegisterAPI.as_view()),
		path('api/auth/login', LoginAPI.as_view()),
		path('api/auth/user', UserAPI.as_view()),
		#Distroy the token on the backend
		path('api/auth/logout', knox_views.LogoutView.as_view(), name='logout'),
]