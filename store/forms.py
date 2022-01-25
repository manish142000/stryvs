from dataclasses import fields
from pyexpat import model
from tabnanny import verbose
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.contrib.auth.models import User
from .models import Product


class ProductRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['name', 'cost', 'image', 'description', 'want_to_rent', 'rent_per_month', 'want_to_sell']

class ProductRentingForm(forms.Form):
    tenure_in_months = forms.IntegerField()


class ProductUpdateForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'cost', 'image', 'description', 'want_to_rent', 'rent_per_month', 'want_to_sell']

    
    