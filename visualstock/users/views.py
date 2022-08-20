from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import LoginForm, SignUpForm

# Create your views here.
def singup_user(request):

    if request.user.is_authenticated:
        return redirect('index')

    signup_form = SignUpForm()

    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)

        if signup_form.is_valid():
            success_message_text = """
                Te has 
                <span class="popup__span">&nbsp;registrado</span>
                <span class="popup__span">&nbsp;correctamente!</span>
            """
            user = signup_form.save()
            messages.success(request, success_message_text)
            login(request, user)

            return redirect('index')

    signup_form_errors = str(signup_form.errors)
    signup_form_errors = signup_form_errors.replace('__all__', 'Errores:')
    for field in signup_form:
        signup_form_errors = signup_form_errors.replace(str(field.name), str(field.label))

    context = {
        'title' : 'Registro',
        'signup_form' : signup_form,
        'signup_form_errors' : signup_form_errors,
    }

    return render(request, "users/signup.html", context)

def login_user(request):

    if request.user.is_authenticated:
        return redirect('index')

    login_form = LoginForm()

    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        
        if login_form.is_valid():
            user = login_form.get_user()
            if user:
                success_message_text = """
                    Haz
                    <span class="popup__span">&nbsp;iniciado&nbsp;</span>
                    sesión
                    <span class="popup__span">&nbsp;correctamente!</span>
                """
                login(request, user)
                messages.success(request, success_message_text)
                return redirect('index')

    login_form_errors = str(login_form.errors)
    login_form_errors = login_form_errors.replace('__all__', 'Errores:')
    for field in login_form:
        login_form_errors = login_form_errors.replace(str(field.name), str(field.label))

    context = {
        'title' : 'Iniciar Sesión',
        'login_form' : login_form,
        'login_form_errors' : login_form_errors
    }
    
    return render(request, "users/login.html", context)

@login_required
def logout_user(request):

    logout(request)
    info_message_text = """
        Haz
        <span class="popup__span">&nbsp;cerrado&nbsp;</span>
        sesión
        <span class="popup__span">&nbsp;correctamente</span>
    """
    messages.info(request, info_message_text)

    return redirect(request.GET.get('next'))