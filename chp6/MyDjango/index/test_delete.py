#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: test_delete.py
@Time: 2018-11-24 14:35
@Last_update: 2018-11-24 14:35
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

def test_delete(request):
    p = Product.objects.filter(id=12)
    p.delete()
    return HttpResponse('name:%s type:%s' % (p.name, p.type_id))