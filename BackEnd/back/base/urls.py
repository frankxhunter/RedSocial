from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginApiView.as_view(), name='login'),
    path('register/', views.RegisterApiView.as_view(), name='register'),
    path('logout/', views.LogoutApiView.as_view(), name='logout'),
    path('', views.allowed_urls, name='home'),
    path('users/', views.UsersApiView.as_view(), name='users'),
    path('users/<str:pk>/', views.UserDetailApiView.as_view(), name='user-detail'),
]
