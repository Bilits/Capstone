from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from home.models import *

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password2 = None
    inlineRadioOptions = forms.CharField(required=True, help_text='Required.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'inlineRadioOptions', )

class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'address', 'dob', 'city', 'postal_code', 'country')

class DepositForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ('tether',)