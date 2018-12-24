from django import forms

from .models import CarPostModel


class CarPostForm(forms.ModelForm):
    images = forms.ImageField(label='Product Images', widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = CarPostModel
        exclude = ('post_owner', 'is_sold', 'post_time')


class CarPostUpdateForm(forms.ModelForm):
    images = forms.ImageField(label='Product Images', required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = CarPostModel
        exclude = ('post_owner', 'post_time')
