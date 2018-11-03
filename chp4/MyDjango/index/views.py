from django.shortcuts import render
from django.http import HttpResponse
import csv

# Create your views here.
def download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachement; filename="somefilename.csv'
    writer = csv.writer(response)
    writer.writerow(['First row', 'A', 'B', 'C'])
    return response

def index(request):
    return HttpResponse("Hello world")

def mydate(request, year, month, day):
    return HttpResponse('%s/%s/%s' % (str(year), str(month), str(day)))

def myyear(request, year):
    return render(request, 'myyear.html')

def myyear_dict(request, year, month):
    return render(request, 'myyear_dict.html', {'month':month})
