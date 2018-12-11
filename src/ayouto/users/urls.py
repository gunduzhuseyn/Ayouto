from django.urls import path, re_path

from .views import (CustomerRegistrationView, ManufacturerRegistrationView, UserLoginView,
                    UserLogoutView,
                    )

urlpatterns = [
    path('man_register/', ManufacturerRegistrationView.as_view(), name='man_register'),
    path('user_register/', CustomerRegistrationView.as_view(), name='user_register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout')
]