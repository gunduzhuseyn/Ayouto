from datetime import date

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
    # TODO: use the whole UserRegistrationForm, with disabled fields
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


class PaymentForm(forms.Form):
    number = forms.CharField(min_length=16, max_length=16, label='Card Number')
    name = forms.CharField(max_length=30, label='Card Holder Name')
    expire_month = forms.ChoiceField(choices=[(x, x) for x in range(1, 13)])
    expire_year = forms.ChoiceField(choices=[(x, x) for x in range(date.today().year, date.today().year + 15)])
    cvv_number = forms.IntegerField(max_value=999, label='CVV Number',
                                    widget=forms.TextInput(attrs={'size':'4'}))
    amount = forms.IntegerField(label='Amount')
