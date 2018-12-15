from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ManufacturerVerificationCodeModel, CustomerModel


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=50, label='Email')
    telephone_no = forms.CharField(max_length=40, label='Phone Number', required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class CustomerProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label='First Name', required=False)
    last_name = forms.CharField(max_length=50, label='Last Name', required=False)

    class Meta:
        model = CustomerModel
        fields = ('first_name', 'last_name', 'telephone_number')


class ManufacturerRegistrationForm(UserRegistrationForm):
    verification_code = forms.CharField(max_length=100, label='Verification Code')
    company_name = forms.CharField(max_length=100, label='Company Name')
    company_address = forms.CharField(max_length=300, label='Company Address')
    company_number = forms.CharField(max_length=50, label='Company Telephone Number')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        code = cleaned_data.get('verification_code')

        if email and code:
            vc = ManufacturerVerificationCodeModel.objects.all().filter(email=email)

            if not vc or code != vc[0].verification_code:
                message = "Your email or verification code does not match our records!"
                self.add_error('verification_code', message)


