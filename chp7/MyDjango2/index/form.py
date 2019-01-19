#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: form.py
@Time: 2019-01-19 22:14
@Last_update: 2019-01-19 22:14
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
from django.core.exceptions import ValidationError

def weights_validate(value):
    if not str(value).isdigit():
        raise ValidationError('please input the right weight')

class ProductForm(forms.Form):
    name = forms.CharField(max_length=20, label='NAME', widget=forms.widgets.TextInput(attrs={'class':'c1'}),
                           error_messages={'required':'name should not be empty'})
    weight = forms.CharField(max_length=50, label='WEIGHT',validators=[weights_validate])
    size = forms.CharField(max_length=50, label='SIZE')

    choices_list = [(i+1,v['type_name']) for i,v in enumerate(Type.objects.values('type_name'))]
    type = forms.ChoiceField(widget=forms.widgets.Select(attrs={'class':'type','size':'4'}),
                             choices=choices_list, label='TYPE')