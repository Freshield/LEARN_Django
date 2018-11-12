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
p = Product()
p.name = '荣耀V9'
p.weight = '111g'
p.size = '120*75*7mm'
p.type_id = 1
p.save()