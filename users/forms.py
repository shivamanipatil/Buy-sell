from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """Extending usercreation form for including email"""
    
    email = forms.EmailField()
    
    class Meta:
        """Specifying model and fields for our form"""
        model = User
        fields = ['username', 'email', 'password1', 'password2']

