from django import forms
# models: user, permissions, group, forms
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
        
