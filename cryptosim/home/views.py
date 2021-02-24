from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            if form.cleaned_data.get('inlineRadioOptions') == 'beginner':
                user.profile.beginner = True
                user.save()
            else:
                user.profile.professional = True
                user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home:login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def LoginView(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home:home')
    else:
        return redirect('register')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

