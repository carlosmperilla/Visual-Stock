import json

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .captcha_img_tag import generate_captcha

from .forms import LoginForm, SignUpForm


def renew_captcha(request):

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        
        captcha_dict = generate_captcha()
        request.session['captcha_error_counter'] = 0
        request.session['captcha'] = captcha_dict['value']
        
        return JsonResponse({'captcha_img': captcha_dict['b64_data']})

def review_captcha(request):

    data = {}

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        captcha_session = request.session.get('captcha')
        if captcha_session and request.body:
            captcha_input = json.loads(request.body).get('captcha_input', '').strip()

            if captcha_session == captcha_input:
                return JsonResponse({'captcha_state': 'success'})
        
        
        data = {'captcha_state': 'error'}
        
        if request.session.get('captcha_error_counter') < 2:
            request.session['captcha_error_counter'] = request.session.get('captcha_error_counter') + 1
        else:
            captcha_dict = generate_captcha()
            request.session['captcha_error_counter'] = 0
            request.session['captcha'] = captcha_dict['value']
            data['captcha_img'] = captcha_dict['b64_data']

        return JsonResponse(data)

# Create your views here.
def singup_user(request):

    if request.user.is_authenticated:
        return redirect('index')

    if request.session.get('captcha'):
        print(request.session.get('captcha', 0))
    
    signup_form = SignUpForm()

    if request.method == 'POST':
        captcha_session = request.session.get('captcha')
        if not captcha_session:
            return redirect('signup')
        
        captcha_input = request.POST.get('captcha', "").strip()
        if captcha_session != captcha_input:
            return redirect('signup')
        else:
            request.session['captcha'] = None

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
    
    captcha_dict = generate_captcha()
    request.session['captcha'] = captcha_dict['value']
    request.session['captcha_error_counter'] = 0

    signup_form_errors = str(signup_form.errors)
    signup_form_errors = signup_form_errors.replace('__all__', 'Errores:')
    for field in signup_form:
        signup_form_errors = signup_form_errors.replace(str(field.name), str(field.label))

    context = {
        'title' : 'Registro',
        'signup_form' : signup_form,
        'signup_form_errors' : signup_form_errors,
        'captcha' : captcha_dict['b64_data']
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