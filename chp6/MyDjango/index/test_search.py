#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: test_search.py
@Time: 2018-11-25 14:39
@Last_update: 2018-11-25 14:39
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
from django.db.models import Q, Sum, Count

def test_search(request):
    p = Product.objects.filter(id__gt=6)
    print('here')
    for i in p:
        print(i.name)
    return HttpResponse('success')