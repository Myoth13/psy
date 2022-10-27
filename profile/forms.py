from django import forms
from django.forms import ModelForm
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UpdateUserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['profile_id', 'user', 'email']


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

