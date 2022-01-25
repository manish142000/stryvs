from dataclasses import fields
from tabnanny import verbose
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.contrib.auth.models import User
from .models import Profile, Appointments
from store.models import Product


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User 
        fields = ['username', 'email', 'password']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image', 'phone', 'address']


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointments 
        fields = ["appointment_date", "appointment_subject", "appointment_time"]



