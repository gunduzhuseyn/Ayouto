from django.urls import path, re_path

from .views import (CustomerRegistrationView, ManufacturerRegistrationView, UserLoginView,
                    UserLogoutView, UserPasswordChangeView, UserPasswordChangeDoneView,
                    UserPasswordResetView, UserPasswordResetDoneView, UserPasswordResetConfirmView,
                    UserPasswordResetCompleteView, )

urlpatterns = [
    path('man_register/', ManufacturerRegistrationView.as_view(), name='man_register'),
    path('user_register/', CustomerRegistrationView.as_view(), name='user_register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('change_password/', UserPasswordChangeView.as_view(), name='password_change'),
    path('change_password/done/', UserPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('reset_password/', UserPasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password/complete/', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
