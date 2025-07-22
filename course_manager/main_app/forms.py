from django import forms
from .models import Location
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['campus']



class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']