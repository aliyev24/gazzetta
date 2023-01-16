from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from django import forms


class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username',)


class LoginUserForm(AuthenticationForm):
    password = forms.CharField()

