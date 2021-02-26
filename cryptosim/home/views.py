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
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from home.models import *
from django.views.generic import FormView
from home.price import *
import json
from django.http import HttpResponse



def get_user(request):
    profile = Profile.objects.get(id = request.user.id)
    return profile

def get_balance(request):
    balance = Wallet.objects.get(id = request.user.id).get_balance
    return balance

def get_total(request):
    balance = Wallet.objects.get(id = request.user.id).get_total
    return balance

def index(request):
    context = {
        'price': get_btc()['price'],
        'change24': get_btc()['change24']
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

@login_required
def dashboard(request):
    amount = 0.0
    alarm = True
    empty = True
    current = float(get_btc()['price'])
    profile = get_user(request)
    if request.is_ajax():
        if request.method == 'POST' and 'amount' in request.POST:
            if request.POST['amount'] != "":
                amount = float(request.POST['amount'])
                amountusd = amount * float(get_btc()['price'])
                if get_user(request).wallet.tether >= amountusd:
                    profile.wallet.tether -= amountusd
                    profile.wallet.bitcoin += amount
                    profile.save()
                    current = float(get_btc()['price']) * amount
                else:
                    alarm = False
                    return HttpResponse(json.dumps({'alarm': alarm}), content_type="application/json")
            else:
                empty = False
                return HttpResponse(json.dumps({'empty': empty}), content_type="application/json")
        else:
            amount = 0
    context = {
        'balance': get_balance(request),
        'total': get_total(request),
        'amount' : amount,
        'current': current,
        
    }
    if get_user(request).professional == True:
        return render(request, 'dashboard-professional.html', context)
        
    else:
        return render(request, 'dashboard-beginner.html', context)

@login_required
def account(request):
    return render(request, 'account-overview.html')

@login_required
def account_deposit(request):
    context = {
        'balance': get_balance(request),
        'total': get_total(request)
    }
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            profile = get_user(request)
            profile.wallet.tether += form.cleaned_data.get('tether')
            profile.save()
            # Problem 
    return render(request, 'account-deposit.html', context)

@login_required
def account_data(request):
    return render(request, 'data-tbi.html')

@login_required
def account_exchange(request):
    context = {
        'price' : get_btc()['price'],
        'balance' : get_balance(request)
    }
    return render(request, 'exchange.html', context)



@login_required
def setting(request):
    profile = get_user(request)
    context = {
        'first_name': profile.first_name,
        'last_name': profile.last_name,
        'email': profile.email,
        'city': profile.city,
        'address': profile.address,
        'dob': profile.dob,
        'country': profile.country,
        'postal_code': profile.postal_code,
    }
    if request.method == 'POST':
        form = PersonalInformationForm(request.POST)
        if form.is_valid():
            profile = get_user(request)
            profile.first_name = form.cleaned_data.get('first_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.email = form.cleaned_data.get('email')
            profile.country = form.cleaned_data.get('country')
            profile.city = form.cleaned_data.get('city')
            profile.postal_code = form.cleaned_data.get('postal_code')
            profile.address = form.cleaned_data.get('address')
            profile.dob = form.cleaned_data.get('dob')
            profile.save()
            return redirect('home:setting')
    return render(request, 'settings.html', context)

