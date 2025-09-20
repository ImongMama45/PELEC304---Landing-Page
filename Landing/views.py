from django.shortcuts import render
from django.http import HttpResponse
from .models import Items_1, Items_2

# Create your views here.

def Landing(request):
    products = Items_1.objects.all()
    formal = Items_2.objects.all()
    context = {'products': products, 'formal' : formal}
    return render(request, 'Landing/home.html', context)