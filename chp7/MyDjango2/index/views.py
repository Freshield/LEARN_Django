from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .form import *

# Create your views here.
def insert_data(request):
    # Type.objects.create(id=1, type_name='phone')
    # Type.objects.create(id=2, type_name='tablet')
    # Type.objects.create(id=3, type_name='smart_wear')
    # Type.objects.create(id=4, type_name='accessor')
    #
    # Product.objects.create(id=1, name='V10', weight='111g', size='157*233*233mm', type_id=1)
    # Product.objects.create(id=2, name='nova', weight='111g', size='157*233*233mm', type_id=1)
    # Product.objects.create(id=3, name='waterplay', weight='111g', size='157*233*233mm', type_id=2)
    # Product.objects.create(id=4, name='changwan', weight='111g', size='157*233*233mm', type_id=2)
    # Product.objects.create(id=5, name='porsche', weight='111g', size='157*233*233mm', type_id=3)
    # Product.objects.create(id=6, name='action_wear', weight='111g', size='157*233*233mm', type_id=3)
    # Product.objects.create(id=7, name='battery', weight='111g', size='157*233*233mm', type_id=4)
    # Product.objects.create(id=8, name='cheng', weight='111g', size='157*233*233mm', type_id=4)
    # Product.objects.create(id=9, name='V10', weight='111g', size='157*233*233mm', type_id=1)
    # Product.objects.create(id=10, name='V10', weight='111g', size='157*233*233mm', type_id=1)
    # Product.objects.create(id=11, name='V10', weight='111g', size='157*233*233mm', type_id=1)

    return HttpResponse('success')


def index(request):
    if request.method == 'GET':
        print('get')
        product = ProductForm()
    else:
        print('post')
        product = ProductForm(request.POST)
        if product.is_valid():
            print('valid')
            name = product['name']
            cname = product.cleaned_data['name']
            print('here')
            print(name)
            print(cname)
            print(product)
            print(product.cleaned_data)
            return HttpResponse('success')
        else:
            print('error')
            error_msg = product.errors.as_json()
            print(error_msg)


    submit = '<input type="submit" value="SUBMIT">'
    print('here1')
    print(locals())
    return render(request, 'data_form.html', locals())
