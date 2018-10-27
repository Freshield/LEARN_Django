from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def mydate(request, year, month, day):
    return HttpResponse('%s/%s/%s' % (str(year), str(month), str(day)))
