from django.shortcuts import render
from django.http import HttpResponse
from django.middleware.csrf import get_token
import csv
import json

# Create your views here.
def index(request):
    return HttpResponse('Hello world')


def download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'atachment; filename="somefilename.csv'
    writer = csv.writer(response)
    writer.writerow(['First row', 'A', 'B', 'C'])
    return response


def test(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.body)
        print(request.body.decode())
        data_dict = eval(json.loads(request.body.decode()))
        print(data_dict)
        return HttpResponse('post')
    else:
        return HttpResponse('get')