#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: myfilter.py
@Time: 2018-11-10 16:23
@Last_update: 2018-11-10 16:23
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from django import template

register = template.Library()

@register.filter
def myreplace(value:str, agrs:str):
    oldValue = agrs.split(':')[0]
    newValue = agrs.split(':')[1]
    return value.replace(oldValue, newValue)