#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: urls.py
@Time: 2018-10-20 17:21
@Last_update: 2018-10-20 17:21
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from django.urls import path, re_path
from . import views
urlpatterns = [
    path('', views.index),
    # path('<year>/<int:month>/<slug:day>', views.mydate),
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='myyear'),
    re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html', views.mydate)
]