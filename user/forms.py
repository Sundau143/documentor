from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'username']

