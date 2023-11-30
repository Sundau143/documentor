from django.contrib.auth import views as auth_views
from user import views
from django.urls import path

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/',  views.register, name='register'),

    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit, name='edit'),
]