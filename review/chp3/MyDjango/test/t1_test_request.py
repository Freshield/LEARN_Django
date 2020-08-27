# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: t1_test_request.py
@Time: 2020-08-27 14:48
@Last_update: 2020-08-27 14:48
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import json
import requests

url = 'http://127.0.0.1:8000/test'
# res = requests.get(url=url)
# print(res.text)
data = [{'name': 'here', 'data': 1}, {'name': 'here1', 'data': 2}]
data = json.dumps(data)
# data = {'data': data}
# headers = {'Content-Type': 'application/json'}
res = requests.post(url=url, json=data)
print(res.text)