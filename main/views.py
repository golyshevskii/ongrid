from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .forms import SignUpForm, LoginForm
from .models import CustomeUser


@login_required(login_url='/login/')
def main_page(request):
    """Function for rendering main page"""

    return render(request, 'base.html')


@login_required(login_url='/login/')
def logout_page(request):
    """Function for render logout process"""
    
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("mainpage")


def login_page(request):
    """Function for render and validate login process"""

    context = {'val_err': None, 'emp_pass': None, 'form': None}

    if request.method == 'POST':
        form = LoginForm(request.POST)

        email = request.POST['email']

        try:
            validate_email(email)
        except ValidationError:
            context['val_err'] = 'Email Address is not valid'

        try:
            user = CustomeUser.objects.get(email=email)
        except:
            messages.info(request, 'Username does not exist!')

        if form.is_valid():
            cd = form.cleaned_data

            user = authenticate(username=cd['email'], password=cd['password'])
            login(request, user)
            return redirect('mainpage')
        else:
            context['emp_pass'] = 'Password required'
    else:
        form = LoginForm()
    
    context['form'] = form

    return render(request, 'login.html', context=context)


def signup_page(request):
    """Function for render and validate sign up process"""

    context = {'val_err': None, 'pass_err': None, 'form': None}

    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        try:
            validate_email(email)
        except ValidationError:
            context['val_err'] = 'Email Address is not valid'

        if password1 and password2 and password1 != password2:
            form = SignUpForm()
            context['pass_err'] = "Passwords don't match"
        elif not password1 or not password2:
            form = SignUpForm()
            context['pass_err'] = "Passwords are empty"
        else:
            form = SignUpForm(request.POST)

            if form.is_valid():
                form.save()
                messages.info(request, "Sign up successfully!")
                return redirect('mainpage')

        context['form'] = form

    return render(request, 'signup.html', context=context)
