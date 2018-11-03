from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv

# Create your views here.
def download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['First row', 'A', 'B', 'C'])
    return response

def login(request):
    return redirect('/')

def index(request):
    return render(request, 'index.html', context={'title': '首页'}, status=500)