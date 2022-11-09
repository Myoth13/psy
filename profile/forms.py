from django import forms
from django.forms import ModelForm
from .models import UserProfile, User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateUserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['profile_id', 'user', 'email']


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

