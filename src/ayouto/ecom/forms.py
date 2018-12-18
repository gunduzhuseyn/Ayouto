from django import forms

from .models import CarPostModel


class CarPostForm(forms.ModelForm):

    class Meta:
        model = CarPostModel
        exclude = ('post_owner', 'is_sold', 'post_time')
