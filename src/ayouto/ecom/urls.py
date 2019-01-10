from django.urls import path, re_path

from .views import (CarPostCreateView, CarPostListView, CarPostDetailView, CarSearchView)

urlpatterns = [
    path('post_create/', CarPostCreateView.as_view(), name='car_post_create'),
    path('home/', CarPostListView.as_view(), name='car_post_list'),
    path('home/search/', CarSearchView.as_view(), name='car_search'),
    re_path('post/(?P<pk>\d+)/$', CarPostDetailView.as_view(), name='car_post_detail'),
]
