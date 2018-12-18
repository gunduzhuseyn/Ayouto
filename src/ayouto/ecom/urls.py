from django.urls import path, re_path

from .views import (CarPostCreateView)

urlpatterns = [
    path('create_post/', CarPostCreateView.as_view(), name='create_post'),
]
