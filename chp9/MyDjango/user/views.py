from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def loginView(request):
    title = 'LOGIN'
    unit_2 = '/user/register.html'
    unit_2_name = 'REGISTER'
    unit_1 = '/user/setpassword.html'
    unit_1_name = 'set password'
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password =request.POST.get('password', '')
        if User.objects.filter(username=username):
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                return redirect('/')
            else:
                tips = 'user or password mistake, please try again'
        else:
            tips = "user don't exist, please registe"

    return render(request, 'user.html', locals())

def registerView(request):
    title = 'REGISTER'
    unit_2 = '/user/login.html'
    unit_2_name = 'LOGIN'
    unit_1 = '/user/setpassword.html'
    unit_1_name = 'SET PASSWORD'
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if User.objects.filter(username=username):
            tips = 'USER EXISTS'
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            tips = 'DONE REGISTER, PLEASE LOGIN'

    return render(request, 'user.html', locals())

def setpasswordView(request):
    title = 'SET PASSWORD'
    unit_2 = '/user/login.html'
    unit_2_name = 'LOGIN'
    unit_1 = '/user/register.html'
    unit_1_name = 'REGISTER'
    new_password = True
    if request.method == 'POST':
        username = request.POST.get('username', '')
        old_password = request.POST.get('password', '')
        new_password = request.POST.get('new_password', '')
        if User.objects.filter(username=username):
            user = authenticate(username=username, password=old_password)
            user.set_password(new_password)
            user.save()
            tips = 'password changed'
        else:
            tips = "user don't exists"

    return render(request, 'user.html', locals())

def logoutView(request):
    logout(request)
    return redirect('/')

