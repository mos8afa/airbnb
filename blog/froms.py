from django import forms
from . models import Post, Category


class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description','image','tags','category']


class AddCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']