from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from .forms import CustomUserCreationForm
from .models import User

def login_view(request):

    # Пересылает пользователей с логином на панель управления
    if request.user.is_authenticated:
        return redirect('dashboard:index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard:index')
        else:
            return render(request, 'accounts/login.html', {
                'message': 'Неверный логин или пароль'
            })
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

def register_view(request):

    # Пересылает пользователей с логином на панель управления
    if request.user.is_authenticated:
        return redirect('dashboard:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard:index')
        else:
            # Проверяет занят никнейм или нет
            username = request.POST['username']
            if User.objects.filter(username=username).exists():
                return render(request, 'accounts/register.html', {
                    'form': form,
                    'message': 'Логин уже занят'
                })
            # Проверяет занята почта или нет
            email = request.POST['email']
            if User.objects.filter(email=email).exists():
                return render(request, 'accounts/register.html', {
                    'form': form,
                    'message': 'Email уже занят'
                })
            password1 = request.POST['password1']
            confirm = request.POST['password2']
            if password1 != confirm:
                return render(request, 'accounts/register.html', {
                    'form': form,
                    'message': 'Пароли не совпадают'
                })

            return render(request, 'accounts/register.html', {
                'form': form,
                'message': 'Неизвестная ошибка'
                })
    elif request.method == 'GET':
        form = CustomUserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})
