from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

# Extend the django in-built UserCreationForm to include email
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # Specify model to interact with form and fields to include 
    class Meta:
        model = User
        fields = ('username', 'email','password1','password2')
        # Saves automatically because email is part of in-builder User model fields

# Form allowing users to update their profiles
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_photo', 'interests']