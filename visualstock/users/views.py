from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import SignUpForm

# Create your views here.
def singup(request):

    if request.user.is_authenticated:
        return redirect('index')

    signup_form = SignUpForm()

    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, 'Te has registrado correctamente!!!')
            # return redirect('index')
        messages.error(request, 'Registro fallido, verifique sus datos ingresados')

    signup_form_errors = str(signup_form.errors)
    for field in signup_form:
        signup_form_errors = signup_form_errors.replace(str(field.name), str(field.label))

    context = {
        'title' : 'Registro',
        'signup_form' : signup_form,
        'signup_form_errors' : signup_form_errors,
    }

    return render(request, "users/signup.html", context)

def login(request):
    context = {}
    return render(request, "users/login.html", context)

# @login_required
def logout_user(request):
    
    logout(request)

    return redirect('login')