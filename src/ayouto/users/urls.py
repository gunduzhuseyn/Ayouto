from django.urls import path, re_path

from .views import (CustomerRegistrationView, ManufacturerRegistrationView, UserLoginView,
                    UserLogoutView, UserPasswordChangeView, UserPasswordChangeDoneView,
                    UserPasswordResetView, UserPasswordResetDoneView, UserPasswordResetConfirmView,
                    UserPasswordResetCompleteView, SellerVerificationView,
                    UserBankAccountView, UserBankAccountUpdateView, UserProfileView, UserProfileUpdateView)

urlpatterns = [
    path('man_register/', ManufacturerRegistrationView.as_view(), name='man_register'),
    path('user_register/', CustomerRegistrationView.as_view(), name='user_register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('password_change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', UserPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('customer_verify/', SellerVerificationView.as_view(), name='customer_verify'),
    path('user_profile/', UserProfileView.as_view(), name='user_profile'),
    path('user_profile/edit/', UserProfileUpdateView.as_view(), name='user_profile_edit'),
    path('user_bank_account/', UserBankAccountView.as_view(), name='user_bank_account'),
    path('user_bank_account/update/', UserBankAccountUpdateView.as_view(), name='user_bank_account_update'),
]
