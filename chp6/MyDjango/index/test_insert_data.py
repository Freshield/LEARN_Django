#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: test_insert_data.py
@Time: 2018-11-12 22:29
@Last_update: 2018-11-12 22:29
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from index.models import *
from django.http import HttpResponse

def test_insert_data(request):
    # t = Type()
    # t.id = 4
    # t.type_name = 'accessory'
    # t.save()

    p = Product()
    p.name = 'steelyard'
    p.weight = '111g'
    p.size = '120*75*7mm'
    p.type_id = 4
    p.save()
    return HttpResponse('name:%s type:%s'%(p.name, p.type_id))
# Product.objects.create(
#     name='荣耀V9', weight='111g', size='120*75*7mm', type_id=1)