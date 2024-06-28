from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request,'mirasolapp/index.html', context)

def login(request):
    context = {}
    return render(request, 'mirasolapp/login.html', context)

def formulario(request):
    context = {}
    return render(request, 'mirasolapp/formulario.html', context)

def noticias(request):
    context = {}
    return render(request, 'mirasolapp/noticias.html', context)

def servicios(request):
    context = {}
    return render(request, 'mirasolapp/servicios.html', context)