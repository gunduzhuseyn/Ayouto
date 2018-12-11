from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetView, PasswordResetDoneView,
                                       PasswordResetConfirmView, PasswordResetCompleteView,
                                       )

from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import UserRegistrationForm, ManufacturerRegistrationForm
from .models import ManufacturerModel


# Registration Views For Customers and Manufacturers
class CustomerRegistrationView(FormView):
    template_name = "users/register.html"
    form_class = UserRegistrationForm
    success_url = '/users/user_register'

    def form_valid(self, form):
        form.save()

        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')

        user = authenticate(username=username, password=raw_password)
        group = Group.objects.get(name='customer')
        group.user_set.add(user)
        login(self.request, user)

        return super().form_valid(form)


class ManufacturerRegistrationView(FormView):
    template_name = "users/register.html"
    form_class = ManufacturerRegistrationForm
    success_url = '/users/man_register'

    def form_valid(self, form):
        form.save()

        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        company_name = form.cleaned_data.get('company_name')
        company_address = form.cleaned_data.get('company_address')
        company_number = form.cleaned_data.get('company_number')

        user = authenticate(username=username, password=raw_password)
        group = Group.objects.get(name='manufacturer')
        group.user_set.add(user)

        manufacturer = ManufacturerModel.objects.create(representative=user, company_name=company_name,
                                                        company_address=company_address, company_number=company_number)
        manufacturer.save()

        login(self.request, user)

        return super().form_valid(form)


# Login View for all users: modified default Django View
class UserLoginView(LoginView):
    template_name = 'users/login.html'


# Logout View for all users: modified default Django View
class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'


# User Password Change Views: modified default Django Views
class UserPasswordChangeView(PasswordChangeView):
    template_name = 'users/password_change.html'


class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'


# User Password Reset Views: modified default Django Views
class UserPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'
    from_email = 'no_reply@ayouto.com'


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'
