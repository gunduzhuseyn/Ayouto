from django.urls import path, re_path

from .views import (CustomerRegistrationView, ManufacturerRegistrationView, UserLoginView,
                    UserLogoutView, UserPasswordChangeView, UserPasswordChangeDoneView,
                    )

urlpatterns = [
    path('man_register/', ManufacturerRegistrationView.as_view(), name='man_register'),
    path('user_register/', CustomerRegistrationView.as_view(), name='user_register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('change_password', UserPasswordChangeView.as_view(), name='password_change'),
    path('change_password_done', UserPasswordChangeDoneView.as_view(), name='password_change_done'),
]