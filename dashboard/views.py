from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def index(request):

    # Если пользователь не залогинен - переслать на начальную страницу
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    return render(request, 'dashboard/index.html')