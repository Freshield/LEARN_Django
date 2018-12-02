#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: form.py
@Time: 2018-12-02 11:46
@Last_update: 2018-12-02 11:46
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from django import forms
from .models import *

class ProductForm(forms.Form):
    name = forms.CharField(max_length=20, label='NAME',)
    weight = forms.CharField(max_length=50, label='WEIGHT')
    size = forms.CharField(max_length=50, label='SIZE')

    choices_list = [(i+1,v['type_name']) for i,v in enumerate(Type.objects.values('type_name'))]
    type = forms.ChoiceField(choices=choices_list, label='TYPE')