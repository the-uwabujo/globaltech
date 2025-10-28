from django.contrib.auth.forms import UserCreationForm
from globalapp.models import Account


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['email','first_name','last_name','phone_number','password1','password2']