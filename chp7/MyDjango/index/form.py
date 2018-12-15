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
from django.core.exceptions import ValidationError

def weights_validate(value):
    if not str(value).isdigit():
        raise ValidationError('please input the right weight')

class ProductForm(forms.Form):
    name = forms.CharField(max_length=20, label='NAME', widget=forms.widgets.TextInput(attrs={'class':'c1'}),
                           error_messages={'required':'name should not be empty'}, initial='yy')
    weight = forms.CharField(max_length=50, label='WEIGHT',validators=[weights_validate], initial='233g')
    size = forms.CharField(max_length=50, label='SIZE', initial='233*233*233mm')

    choices_list = [(i+1,v['type_name']) for i,v in enumerate(Type.objects.values('type_name'))]
    type = forms.ChoiceField(widget=forms.widgets.Select(attrs={'class':'type','size':'4'}),
                             choices=choices_list, label='TYPE', initial=(1,'phone'))

class ProductModelForm(forms.ModelForm):
    productId = forms.CharField(max_length=20, label='product sequence')
    class Meta:
        model = Product
        fields = ['name', 'weight', 'size', 'type']
        exclude = []
        labels = {
            'name': 'NAME',
            'weight': 'WEIGHT',
            'size': 'SIZE',
            'type': 'TYPE'
        }
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'c1'}),
        }
        field_classes = {
            'name': forms.CharField
        }
        help_texts = {
            'name': ''
        }
        error_messages = {
            '__all__': {'required': 'please input something',
                        'invalid': 'please check the input'},
            'weight': {'required': 'please input the weights',
                       'invalid': 'please check the value'}
        }

    def clean_weight(self):
        data = self.cleaned_data['weight']
        return data+'g'