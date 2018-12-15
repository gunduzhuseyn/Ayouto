from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetView, PasswordResetDoneView,
                                       PasswordResetConfirmView, PasswordResetCompleteView,
                                       )

from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import (UserRegistrationForm, ManufacturerRegistrationForm,
                    CustomerProfileUpdateForm,)
from .models import (ManufacturerModel, CustomerModel,)


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


# TODO: customer/seller verification
class CustomerProfileView(TemplateView):
    template_name = 'users/customer_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = CustomerModel.objects.all().get(user=self.request.user)

        context['customer'] = customer

        return context


# TODO: customer/seller verification
class CustomerProfileUpdateView(FormView):
    template_name = "users/customer_profile_update.html"
    form_class = CustomerProfileUpdateForm
    success_url = reverse_lazy('user_profile')

    def get_customer(self):
        customer = CustomerModel.objects.get(user=self.request.user)

        return customer

    def get_initial(self):
        initial = super(CustomerProfileUpdateView, self).get_initial()
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name
        initial['telephone_number'] = self.get_customer().telephone_number

        return initial

    def form_valid(self, form):
        # TODO: push the saving functionality to form.save()
        customer = self.get_customer()
        customer.user.first_name = form.cleaned_data.get('first_name')
        customer.user.last_name = form.cleaned_data.get('last_name')
        customer.telephone_number = form.cleaned_data.get('telephone_number')
        customer.user.save()
        customer.save()

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

