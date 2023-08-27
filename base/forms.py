from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import BlogPost,ContactMessages

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class BlogForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessages
        fields = '__all__'