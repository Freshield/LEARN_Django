from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def hello_world(request):
    return HttpResponse('hello world')

def index(request):
    username = request.user.username
    if username:
        type_list = Type.objects.values('type_name').distinct()
        name_list = Product.objects.values('name', 'type__type_name')
        return render(request, 'index.html', locals())
    else:
        return redirect('/user/login.html')

def insert_data(request):
    Type.objects.create(id=1, type_name='phone')
    Type.objects.create(id=2, type_name='tablet')
    Type.objects.create(id=3, type_name='smart_wear')
    Type.objects.create(id=4, type_name='accessor')

    Product.objects.create(id=1, name='V10', weight='111g', size='157*233*233mm', type_id=1)
    Product.objects.create(id=2, name='nova', weight='111g', size='157*233*233mm', type_id=1)
    Product.objects.create(id=3, name='waterplay', weight='111g', size='157*233*233mm', type_id=2)
    Product.objects.create(id=4, name='changwan', weight='111g', size='157*233*233mm', type_id=2)
    Product.objects.create(id=5, name='porsche', weight='111g', size='157*233*233mm', type_id=3)
    Product.objects.create(id=6, name='action_wear', weight='111g', size='157*233*233mm', type_id=3)
    Product.objects.create(id=7, name='battery', weight='111g', size='157*233*233mm', type_id=4)
    Product.objects.create(id=8, name='cheng', weight='111g', size='157*233*233mm', type_id=4)
    Product.objects.create(id=9, name='V10', weight='111g', size='157*233*233mm', type_id=1)
    Product.objects.create(id=10, name='V10', weight='111g', size='157*233*233mm', type_id=1)
    Product.objects.create(id=11, name='V10', weight='111g', size='157*233*233mm', type_id=1)

    return HttpResponse('success')
