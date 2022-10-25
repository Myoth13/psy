from django import forms
from django.forms import ModelForm
from .models import UserProfile


class UpdateUserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['profile_id', 'user', 'email']

