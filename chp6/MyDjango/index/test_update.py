#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: test_update.py
@Time: 2019-01-17 14:28
@Last_update: 2019-01-17 14:28
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from .models import *
from django.http import HttpResponse

def test_update(request):
    p = Product.objects.get(id=12)
    p.name = 'v9999'
    p.save()
    return HttpResponse('name:%s type:%s'%(p.name, p.type_id))