from django.urls import path, re_path

from .views import (CustomerRegistrationView, ManufacturerRegistrationView)

urlpatterns = [
    path('man_register/', ManufacturerRegistrationView.as_view(), name='man_register'),
    path('user_register/', CustomerRegistrationView.as_view(), name='user_register'),
]