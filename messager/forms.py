from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from .models import AltUser  # Replace with your custom user model if applicable


# class GroupForm(forms.ModelForm):
#     class Meta:
#         model = Room
#         fields = ['name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'pfimage']

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User  # Use the default User model or your custom user model
        fields = ['username', 'password1', 'password2']