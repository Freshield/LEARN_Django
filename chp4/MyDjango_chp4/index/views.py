from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Product
import csv

# Create your views here.
def download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['First row', 'A', 'B', 'C'])
    return response

def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return redirect('/')
    else:
        if request.GET.get('name'):
            name = request.GET.get('name')
        else:
            name = 'Everyone'
        return HttpResponse('username is %s' % (name))

def index(request):
    type_list = Product.objects.values('type').distinct()
    name_list = Product.objects.values('name', 'type')
    title = '首页'
    # context = {'title': '首页', 'type_list':type_list, 'name_list':name_list}
    # return render(request, 'index.html', context=context, status=200)
    return render(request, 'index.html', context=locals(), status=200)

class ProductList(ListView):
    context_object_name = 'type_list'
    template_name = 'index.html'
    # queryset = Product.objects.values('type').distinct()

    def get_queryset(self):
        print(self.kwargs['id'])
        print(self.kwargs['name'])
        print(self.request.method)
        type_list = Product.objects.values('type').distinct()
        return type_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_list'] = Product.objects.values('name', 'type')
        return context