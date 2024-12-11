from django import forms
from .models import Room
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class GroupForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']