from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomeUser


class LoginForm(forms.Form):
    """Form for login user"""

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    """Form for new user registration"""

    email = forms.EmailField()

    class Meta:
        model = CustomeUser
        fields = ['email', 'password1', 'password2']
    