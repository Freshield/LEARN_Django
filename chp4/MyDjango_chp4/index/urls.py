#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: urls.py
@Time: 2018-11-03 16:00
@Last_update: 2018-11-03 16:00
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
from . import views

urlpatterns = [
    path('download.html', views.download),
    path('login.html', views.login),
    path('index/', views.ProductList.as_view()),
    path('index/<id>.html', views.ProductList.as_view(), {'name':'phone'}),
    path('', views.index)
]