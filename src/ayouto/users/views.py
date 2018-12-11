from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group

from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import UserRegistrationForm, ManufacturerRegistrationForm
from .models import ManufacturerModel


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
