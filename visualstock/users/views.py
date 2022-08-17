from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def singup(request):
    context = {}
    return render(request, "users/signup.html", context)

def login(request):
    context = {}
    return render(request, "users/login.html", context)

def logout_user(request):
    
    logout(request)

    return redirect('login')