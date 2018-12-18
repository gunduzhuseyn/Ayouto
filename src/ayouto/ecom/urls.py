from django.urls import path, re_path

from .views import (CarPostCreateView, CarPostListView, CarPostDetailView)

urlpatterns = [
    path('post_create/', CarPostCreateView.as_view(), name='car_post_create'),
    path('home/', CarPostListView.as_view(), name='car_post_list'),
    re_path('post/(?P<pk>\d+)/$', CarPostDetailView.as_view(), name='car_post_detail'),
]
