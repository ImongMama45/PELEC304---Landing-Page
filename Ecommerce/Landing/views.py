from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Landing(request):
    return HttpResponse('Hilo world')

def Home(request):
    return render(request, 'Landing/home.html')