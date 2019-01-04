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
    return HttpResponse('registerView')

def setpasswordView(request):
    return HttpResponse('setpasswordView')

def logoutView(request):
    return HttpResponse('logoutView')

