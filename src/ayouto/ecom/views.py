from django.shortcuts import render

from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import (CarPostModel,)

from .forms import (CarPostForm,)


class CarPostCreateView(FormView):
    form_class = CarPostForm
    template_name = 'ecom/car_post_create.html'
    success_url = '/home'

    def form_valid(self, form):
        car_post = form.save(commit=False)
        car_post.post_owner = self.request.user
        car_post.save()

        return super().form_valid(form)


class CarPostDetailView(DetailView):
    model = CarPostModel
    template_name = 'ecom/car_post_detail.html'
    context_object_name = 'car_post'


class CarPostListView(ListView):
    model = CarPostModel
    paginate_by = 25
    template_name = 'ecom/car_post_list.html'
    context_object_name = 'car_post_list'
    ordering = ['-post_time']

    def get_queryset(self):
        return CarPostModel.objects.filter(is_sold=False).order_by('-post_time')




