from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=40)
    password1 = forms.CharField(max_length=40, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=40, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
