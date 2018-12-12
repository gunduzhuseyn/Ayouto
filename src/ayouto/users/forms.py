from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ManufacturerModel


class UserRegistrationForm(UserCreationForm):
    telephone_no = forms.CharField(max_length=40, label='Phone Number', required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class ManufacturerRegistrationForm(UserRegistrationForm):
    verification_code = forms.CharField(max_length=100, label='Verification Code')
    company_name = forms.CharField(max_length=100, label='Company Name')
    company_address = forms.CharField(max_length=300, label='Company Address')
    company_number = forms.CharField(max_length=50, label='Company Telephone Number')

