from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    context={}
    return render(request, 'M_C/index.html', context)

def login(request):
    context={}
    return render(request, 'M_C/login.html', context)

def noticias(request):
    context={}
    return render(request, 'M_C/noticias.html', context)

def servicios(request):
    context={}
    return render(request, 'M_C/servicos.html', context)

def formulario(request):
    context={}
    return render(request, 'M_C/formulario.html', context)
