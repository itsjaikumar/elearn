from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LessonForm(forms.ModelForm):
    class Meta:
        model= Lesson
        fields= '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LessonForm2(forms.ModelForm):
    class Meta:
        model= Lesson
        fields= '__all__'