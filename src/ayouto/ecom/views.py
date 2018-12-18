from django.shortcuts import render

from django.views.generic.edit import FormView

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



