from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetView, PasswordResetDoneView,
                                       PasswordResetConfirmView, PasswordResetCompleteView,
                                       )

from django.core.files.storage import FileSystemStorage

from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView

from .forms import (UserRegistrationForm, ManufacturerRegistrationForm,
                    CustomerProfileUpdateForm, ManufacturerProfileUpdateForm, PaymentForm,)
from .models import (ManufacturerModel, CustomerModel, UserBankAccount)


def is_user_manufacturer(user):
    return user.groups.all()[0].name == 'manufacturer'


def get_model_user_object(user):
    if is_user_manufacturer(user):
        return ManufacturerModel.objects.get(user=user)
    else:
        return CustomerModel.objects.get(user=user)


# TODO: seller verification
# Verification View for the customers who want to sell second hand cars
class SellerVerificationView(TemplateView):
    template_name = 'users/seller_verification.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        message = ''
        customer = CustomerModel.objects.all().get(user=self.request.user)      # assume customer exists
        status = customer.seller_status

        if customer.telephone_number is None:
            message = 'You have to provide your phone number first. Please do so from your profile page.'
        elif status == 0:
            customer.seller_status = 1
            customer.save()
            message = 'Your request was successful. Our staff will reach you'
        elif status == 1:
            message = 'Your request has been taken into consideration already. Please wait for our staff to reach you'
        elif status == 2:
            message = 'Your account has been verified by our staff already.'

        context['message'] = message
        return context


# Registration Views For Customers and Manufacturers
class CustomerRegistrationView(FormView):
    template_name = "users/register.html"
    form_class = UserRegistrationForm
    success_url = '/users/user_register'

    def form_valid(self, form):
        form.save()

        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        telephone_number = form.cleaned_data.get('telephone_number')

        user = authenticate(username=username, password=raw_password)
        group = Group.objects.get(name='customer')
        group.user_set.add(user)

        user_account = UserBankAccount.objects.create(user=user, balance=0)
        user_account.save()

        customer = CustomerModel.objects.create(user=user, seller_status=0, telephone_number=telephone_number)
        customer.save()

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
        telephone_number = form.cleaned_data.get('telephone_number')
        company_name = form.cleaned_data.get('company_name')
        company_address = form.cleaned_data.get('company_address')
        company_number = form.cleaned_data.get('company_number')

        user = authenticate(username=username, password=raw_password)
        group = Group.objects.get(name='manufacturer')
        group.user_set.add(user)

        user_account = UserBankAccount.objects.create(user=user, balance=0)
        user_account.save()

        manufacturer = ManufacturerModel.objects.create(user=user, company_name=company_name,
                                                        telephone_number=telephone_number,
                                                        company_address=company_address, company_number=company_number)
        manufacturer.save()

        login(self.request, user)

        return super().form_valid(form)


# TODO: authenticate users
class UserProfileView(TemplateView):
    template_name = 'users/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['profile_owner'] = get_model_user_object(self.request.user)
        context['user'] = self.request.user
        context['is_manufacturer'] = is_user_manufacturer(self.request.user)

        return context


class UserProfileUpdateView(FormView):
    template_name = 'users/user_profile_update.html'
    form_class = ManufacturerProfileUpdateForm
    success_url = reverse_lazy('user_profile')

    def get_form_class(self):
        if is_user_manufacturer(self.request.user):
            return ManufacturerProfileUpdateForm
        else:
            return CustomerProfileUpdateForm

    def get_initial(self):
        initial = super(UserProfileUpdateView, self).get_initial()
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name

        model_user = get_model_user_object(self.request.user)
        initial['telephone_no'] = model_user.telephone_number

        if is_user_manufacturer(self.request.user):
            initial['company_name'] = model_user.company_name
            initial['company_address'] = model_user.company_address
            initial['company_number'] = model_user.company_number

        return initial

    def form_valid(self, form):
        model_user = get_model_user_object(self.request.user)
        model_user.user.first_name = form.cleaned_data.get('first_name')
        model_user.user.last_name = form.cleaned_data.get('last_name')
        model_user.user.save()

        model_user.telephone_number = form.cleaned_data.get('telephone_no')
        model_user.profile_image = form.cleaned_data.get('profile_image')

        if is_user_manufacturer(self.request.user):
            model_user.company_name = form.cleaned_data.get('company_name')
            model_user.company_address = form.cleaned_data.get('company_address')
            model_user.company_number = form.cleaned_data.get('company_number')

        model_user.save()

        return super().form_valid(form)


class UserBankAccountView(TemplateView):
    template_name = 'users/bank_account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = UserBankAccount.objects.get(user=self.request.user)

        return context


class UserBankAccountUpdateView(FormView):
    template_name = 'users/bank_account_update.html'
    form_class = PaymentForm
    success_url = reverse_lazy('user_bank_account')

    def form_valid(self, form):
        account = UserBankAccount.objects.get(user=self.request.user)
        account.balance += form.cleaned_data.get('amount')
        account.save()

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

