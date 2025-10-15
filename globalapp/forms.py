from django.contrib.auth.forms import UserCreationForm
from .models import Account
from django import forms

class RegistrationForm(UserCreationForm):
  class Meta:
    model = Account
    fields =['email', 'password1','password2']