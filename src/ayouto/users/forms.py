from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ManufacturerModel


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class ManufacturerRegistrationForm(UserRegistrationForm):
    company_name = forms.CharField(max_length=100, label='Company Name')
    company_address = forms.CharField(max_length=300, label='Company Address')
    company_number = forms.CharField(max_length=50, label='Company Telephone Number')

