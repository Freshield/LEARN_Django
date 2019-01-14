from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    type_list = Product.objects.values('type').distinct()
    name_list = Product.objects.values('name', 'type')
    title = '首页'
    return render(request, 'index.html', context=locals(), status=200)