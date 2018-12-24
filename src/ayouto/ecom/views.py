from django.views.generic.edit import FormView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.urls import reverse

from .models import (CarPostModel, ImageModel)

from .forms import (CarPostForm, CarPostUpdateForm)


class CarPostCreateView(FormView):
    form_class = CarPostForm
    template_name = 'ecom/car_post_create.html'
    success_url = '/home'

    def form_valid(self, form):
        car_post = form.save(commit=False)
        car_post.post_owner = self.request.user
        car_post.save()

        images = self.request.FILES.getlist('images')

        for image in images:
            img = ImageModel.objects.create(car_post=car_post, image=image)
            img.save()

        return super().form_valid(form)


class CarPostUpdateView(UpdateView):
    model = CarPostModel
    form_class = CarPostUpdateForm
    template_name = 'ecom/car_post_update.html'

    def get_success_url(self):
        return reverse('car_post_detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        images = self.request.FILES.getlist('images')

        for image in images:
            img = ImageModel.objects.create(car_post=self.object, image=image)
            img.save()

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




