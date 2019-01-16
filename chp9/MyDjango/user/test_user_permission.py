#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: test_user_permission.py
@Time: 2019-01-16 22:00
@Last_update: 2019-01-16 22:00
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from user.models import MyUser
from django.http import HttpResponse

def test_user_permission(request):
    user = MyUser.objects.filter(username='yangyu')[0]
    res = user.has_perm('index.add_product')
    return HttpResponse(res)