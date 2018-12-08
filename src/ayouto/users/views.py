from django.shortcuts import render
from django.views.generic import TemplateView

class RegisterView(TemplateView):
    template_name = "users/register.html"


class ManRegisterView(RegisterView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = 'manufacturer dude'
        return context


class UserRegisterView(RegisterView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = 'normal dude'
        return context
