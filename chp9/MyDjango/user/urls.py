#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: urls.py
@Time: 2019-01-04 16:34
@Last_update: 2019-01-04 16:34
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from django.urls import path
from . import views, test_user_permission

urlpatterns = [
    path('login.html', views.loginView, name='login'),
    path('register.html', views.registerView, name='register'),
    path('setpassword.html', views.setpasswordView, name='setpassword'),
    path('logout.html', views.logoutView, name='logout'),
    path('findPassword.html', views.findPassword, name='findPassword'),
    path('user_form_register.html', views.user_form_register, name='user_form_register'),
    path('test_user_permission', test_user_permission.test_user_permission)
]