from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomeUser


class SignUpForm(UserCreationForm):
    """Form for new user registration"""

    email = forms.EmailField()

    class Meta:
        model = CustomeUser
        fields = ['email', 'password1', 'password2']
    