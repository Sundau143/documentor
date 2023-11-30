from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, LoginForm, EditUserForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'user/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('profile')
    else:
        return render(request, 'user/login.html', {'error_message': 'Невірний логін або пароль'})
    return render(request, 'user/login.html', {'form': form})

@login_required
def logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    user = get_object_or_404(User, pk=request.user.id)
    return render(request, "user/profile.html", {"user": user})

@login_required
def edit(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            #return redirect('user/profile')
            return redirect(reverse('profile'))
    else:
        form = EditUserForm()
    return render(request, 'user/edit.html', {'form': form})



