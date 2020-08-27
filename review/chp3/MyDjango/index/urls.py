# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: urls.py
@Time: 2020-08-27 14:33
@Last_update: 2020-08-27 14:33
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
    path('', views.index),
    path('index', views.index),
    path('download.html', views.download),
    path('test', views.test)
]