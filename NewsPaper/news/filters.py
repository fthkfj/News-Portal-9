from django_filters import FilterSet, DateFilter, CharFilter
from .models import Post
from django import forms


class PostFilter(FilterSet):
    DateCreation = DateFilter(field_name='DateCreation', lookup_expr='gt', label='Дата',
                              widget=forms.DateInput(format='d.M.Y', attrs={'type': 'data'}))
    title = CharFilter(label='Название', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['authors', 'DateCreation', 'title', 'text']


