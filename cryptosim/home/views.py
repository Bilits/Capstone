from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from django.template.loader import render_to_string
from .tokens import account_activation_token
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

api = cg.get_price(ids='bitcoin', vs_currencies='cad', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')

def index(request):
    context = {
        'price': api['bitcoin']['cad'],
        'change24': api['bitcoin']['cad_24h_change']
    }
    if request.user.is_authenticated:
        return render(request, "index-loggedin.html", context)
    else:
        return render(request, "index.html", context)
        

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('home:login')
    else:
        return render(request, 'activation_invalid.html')

def activation_sent_view(request):
    return render(request, 'activation_sent.html')


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
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            message = render_to_string('activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('home:activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def LoginView(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return redirect('register')

@login_required
def dashboard(request):
    user = User.objects.get(id = request.user.id)
    if user.profile.professional == True:
        return render(request, 'dashboard-professional.html')
    else:
        return render(request, 'dashboard-beginner.html')

