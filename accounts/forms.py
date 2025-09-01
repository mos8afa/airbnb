from django import forms
from . models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from property.models import Property , Category , Place


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','phone_number','address']

class AddCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class AddPlace(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name','image']


class AddList(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'price_per_day','description','image','place','category','created_at']
