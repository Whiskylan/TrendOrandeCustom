from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

# Create your views here.
def register(request: HttpRequest):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', context={
        'title':'Sign Up',
        'form': form,
    })

def login_user(request: HttpRequest):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', context={
        'title': 'Sign In',
        'form': form,

    })
        
def logout_user(request):
    logout(request)
    return render(request, 'base.html')

