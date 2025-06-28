# req/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']  # email dihapus
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None
        }
        labels = {
            'username': 'Username',
            'password1': 'Password',
            'password2': 'ulangi Password'
        }


