from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import UserRegistrationForm
from django.views.generic.edit import FormView


class CustomerRegistrationView(FormView):
    template_name = "users/register.html"
    form_class = UserRegistrationForm
    success_url = '/users/user_register'

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)

