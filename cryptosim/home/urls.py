from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", auth_views.LoginView.as_view(template_name='signin.html'), name="login"),
    path("logout", auth_views.LogoutView.as_view(template_name='signin.html'), name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register", views.register, name="register"),
]