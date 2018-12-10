from django.urls import path, re_path

from .views import (CustomerRegistrationView)

urlpatterns = [
    # path('man_register/', ManRegisterView.as_view(), name='man_register'),
    path('user_register/', CustomerRegistrationView.as_view(), name='user_register'),
]