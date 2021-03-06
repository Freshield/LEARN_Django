from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
import random
from .form import MyUserCreationForm
from .models import MyUser

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
        if MyUser.objects.filter(username=username):
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
        if MyUser.objects.filter(username=username):
            tips = 'USER EXISTS'
        else:
            user = MyUser.objects.create_user(username=username, password=password)
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
        if MyUser.objects.filter(username=username):
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


def findPassword(request):
    button = 'get verification code'
    new_password = False
    if request.method == 'POST':
        username = request.POST.get('username', 'root')
        print(username)
        VerificationCode = request.POST.get('VerificationCode', '')
        password = request.POST.get('password', '')
        user = MyUser.objects.filter(username=username)
        if not user:
            tips = "user: %s don't exist" % username
        else:
            if not request.session.get('VerificationCode', ''):
                button = 'reset password'
                tips = 'verificaiton code sent'
                new_password = True
                VerificationCode = str(random.randint(1000, 9999))
                request.session['VerificationCode'] = VerificationCode
                user[0].email_user('reset password', VerificationCode)
            elif VerificationCode == request.session.get('VerificationCode'):
                print(password)
                # dj_ps = make_password(password, None, 'pbkdf2_sha256')
                # print(dj_ps)
                # user[0].password = dj_ps
                print(user)
                user[0].set_password(password)
                user[0].save()
                del request.session['VerificationCode']
                tips = 'password was reset'
            else:
                tips = 'Verification code error, please reget'
                new_password = False
                del request.session['VerificationCode']

    return render(request, 'findPassword.html', locals())

def user_form_register(request):
    if request.method == 'POST':
        user = MyUserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            tips = 'success'
            user = MyUserCreationForm()
    else:
        user = MyUserCreationForm()

    return render(request, 'user_form_register.html', locals())

