from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

@login_required
def register_view(request):
    return render(request, 'register.html')

@login_required
def home_view(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# Oturum verisi ekleme
def add_session_data(request):
    request.session['key'] = 'value'
    return HttpResponse('Session data added.')

# Oturum verisi okuma
def read_session_data(request):
    value = request.session.get('key', 'Default Value')
    return HttpResponse(f'Session data: {value}')

# Çerez ekleme
def add_cookie(request):
    response = HttpResponse('Cookie added.')
    response.set_cookie('key', 'value', max_age=3600)  # 1 saatlik çerez
    return response

# Çerez okuma
def read_cookie(request):
    value = request.COOKIES.get('key', 'Default Value')
    return HttpResponse(f'Cookie value: {value}')
