__author__ = 'connor'
from django.forms import ModelForm
from blog.models import Category, Blog


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title']


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'category']