from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .forms import SignUpForm


@login_required(login_url='/login/')
def main_page(request):
    """Function for rendering main page"""

    return render(request, 'base.html')


def login_page(request):
    """Function for render and validate login process"""

    context = {'val_err': None, 'emp_pass': None}

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            validate_email(email)
        except ValidationError:
            context['val_err'] = 'Email Address is not valid'

        if password:
            user = authenticate(request, email=email, password=password)
            login(request, user)
            return redirect('mainpage')
        else:
            context['emp_pass'] = 'Password required'

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

        if (password1 and password2 and password1 != password2) or (password1 is None or password2 is None):
            form = SignUpForm()
            context['pass_err'] = "Passwords don't match or they are empty"    
        else:
            form = SignUpForm(request.POST)

            if form.is_valid():
                form.save()

                return redirect('mainpage')

        context['form'] = form

    return render(request, 'signup.html', context=context)
