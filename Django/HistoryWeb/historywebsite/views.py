from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout #untuk login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterUserForm

def index(request):
    context = {
        'judul': 'MyHome',
        'heading': 'Selamat Datang di halaman homeeee',
    }
    return render(request, 'index.html', context)


def register_user(request):
    if request.method == 'POST':
        reg_user = RegisterUserForm(request.POST or None)
        if reg_user.is_valid():
            reg_user.save()
            messages.success(request, 'User Baru Berhasil Disimpan')
            return redirect('index')
        else:
            messages.error(request, 'User Baru Gagal Disimpan')
    else:
        reg_user = RegisterUserForm()
    context = {
        'judul': 'Register User',
        'reg_user': reg_user
    }
    return render(request, 'register.html', context)


def login_user(request):
    context = {
        'judul': 'Login User',
    }
    if request.user.is_authenticated:   #klo sudah login mau url login,bakal balik ke index
        return redirect('index')
    if request.method == 'POST':
        user_input = request.POST.get('username')
        passwd_input = request.POST.get('password')
        user = authenticate(username=user_input, password=passwd_input)
        if user is not None:
            login(request, user)
            messages.success(request,'Login berhasil')
            return redirect('index')
        else:
            messages.error(request,'Login gagal')
            return redirect('login')
    return render(request, 'login.html', context)


@login_required(login_url='/')
def logout_user(request):
    context = {
        'judul': 'Logout',
    }
    # user = request.user
    # if not user.is_authenticated:   #klo sudah  login mau urllogin,bakal balik ke index
    #     return redirect('index')
    if request.method == 'POST':
        if request.POST['keluar'] == 'Logout':
            messages.success(request,'Logout kau sudah berhasil')
            logout(request)
            return redirect('index')
    return render(request,'logout.html',context)
