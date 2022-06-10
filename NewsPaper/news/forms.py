from django.forms import ModelForm
from .models import Post, Category
from django import forms


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['authors', 'title', 'text']
        widgets = {
            'authors': forms.HiddenInput(),
        }


class Subscribe(ModelForm):
    class Meta:
        model = Category
        fields = ['category', 'subscribers']
        widgets = {
            'users': forms.HiddenInput()
        }




