from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


@login_required(login_url='/login/')
def main_page(request):
    return render(request, 'base.html')


def login_page(request):
    context = {'val_err': None, 'emp_pass': None}

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            validate_email(email)
        except ValidationError:
            context['val_err'] = 'Email address is not valid'

        if password:
            user = authenticate(request, email=email, password=password)
            login(request, user)
            return redirect('main:mainpage')
        else:
            context['emp_pass'] = 'Password required'

    return render(request, 'login.html', context=context)
