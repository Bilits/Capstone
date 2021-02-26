from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from . import views
from home.views import *

urlpatterns = [
    path("", views.index, name="index"),
    path("login", auth_views.LoginView.as_view(template_name='signin.html'), name="login"),
    path("logout", auth_views.LogoutView.as_view(template_name='index.html'), name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/account", views.account, name="account"),
    path("dashboard/account/deposit", views.account_deposit, name="account_deposit"),
    path("dashboard/account/signals", views.signals, name="signals"),
    path("dashboard/account/exchange", views.account_exchange, name="account_exchange"),
    path("dashboard/account/settings", views.setting, name="setting"),
    path("register", views.register, name="register"),
    path("activation-sent", views.activation_sent_view, name="activation-sent"),
    path('sent/', activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
]