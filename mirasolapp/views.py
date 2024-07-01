from django.shortcuts import render, redirect, get_object_or_404
import uuid
from .models import Servicio, Noticia 

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
    noticias = Noticia.objects.all()
    return render(request, 'mirasolapp/noticias.html', {'noticias': noticias})

def vistaNoticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'crud/vistaNoticias.html', {'noticias': noticias})

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'mirasolapp/servicios.html', {'servicios': servicios})

<<<<<<< HEAD
=======

>>>>>>> a5867fd89b862c93c1c6cf5d9f5fd47164572854
def seleccionVista(request):
    context = {}
    return render(request, 'crud/seleccionVista.html', context)

def vistaServicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'crud/vistaServicios.html', {'servicios': servicios})

def agregarNoticia(request):
    if request.method == "POST":
        id_noticia = request.POST.get("id_noticia")
        titular = request.POST.get("titular")
        breve_desc = request.POST.get("breve_desc")
        noticia = request.POST.get("noticia")
        fecha = request.POST.get("fecha")
        imagen = request.FILES.get("imagen")

        if Noticia.objects.filter(id_noticia=id_noticia).exists():
            context = {'error': 'ID de noticia ya existe, por favor ingrese un ID único'}
            return render(request, 'crud/agregarNoticia.html', context)

        noticia = Noticia(
            id_noticia=id_noticia,
            titular=titular,
            breve_desc=breve_desc,
            noticia=noticia,
            fecha=fecha,
            imagen=imagen
        )

        noticia.save()

        context = {'mensaje': 'OK, datos guardados con éxito'}
        return render(request, 'crud/noticia.html', context)
    else:
        context = {}
        return render(request, 'crud/agregarNoticia.html', context)
    
def agregarServicio(request):
    if request.method == "POST":
        id_servicio = request.POST.get("id_servicio")
        titulo = request.POST.get("titulo")
        valor = request.POST.get("valor")
        telefono = request.POST.get("telefono")
        Email = request.POST.get("Email")
        imagen = request.FILES.get("imagen")

        if Servicio.objects.filter(id_servicio=id_servicio).exists():
            context = {'error': 'ID de servicio ya existe, por favor ingrese un ID único'}
            return render(request, 'crud/agregarServicio.html', context)

        servicio = Servicio(
            id_servicio=id_servicio,
            titulo=titulo,
            valor=valor,
            telefono=telefono,
            Email=Email,
            imagen=imagen
        )

        servicio.save()

        context = {'mensaje': 'OK, datos guardados con éxito'}
        return render(request, 'crud/servicio.html', context)
    else:
        context = {}
        return render(request, 'crud/agregarServicio.html', context)



def modificarNoticia(request, id_noticia):
    noticia = get_object_or_404(Noticia, id_noticia=id_noticia)
    
    if request.method == 'POST':
        noticia.titular = request.POST['titular']
        noticia.breve_desc = request.POST['breve_desc']
        noticia.noticia = request.POST['noticia']
        noticia.fecha = request.POST['fecha']
        
        if 'nueva_imagen' in request.FILES:
            noticia.imagen = request.FILES['nueva_imagen']
        
        noticia.save()
        return redirect('adminNoticias')  # Redirect to the admin page after saving changes
    
    return render(request, 'crud/modificarNoticia.html', {"noticia": noticia})



def modificarServicio(request, id_servicio):
    servicio = get_object_or_404(Servicio, id_servicio=id_servicio)
    
    if request.method == 'POST':
        servicio.titulo = request.POST['titulo']
        servicio.valor = request.POST['valor']
        servicio.telefono = request.POST['telefono']
        servicio.Email = request.POST['Email']
        
        if 'nueva_imagen' in request.FILES:
            servicio.imagen = request.FILES['nueva_imagen']
        
        servicio.save()
        return redirect('adminServicios')  # Redirige a la página de administración después de guardar los cambios
    
    return render(request, 'crud/modificarServicio.html', {"servicio": servicio})

def eliminarServicio(request, id_servicio):
    servicio = get_object_or_404(Servicio, id_servicio=id_servicio)
    servicio.delete()

    return redirect('adminServicios') 

def eliminarNoticia(request, id_noticia):
    noticia = get_object_or_404(Noticia, id_noticia=id_noticia)
    noticia.delete()

    return redirect('adminNoticias') 

def adminNoticias(request):
    noticias = Noticia.objects.all()
    context = {'noticias': noticias}
    return render(request, 'crud/adminNoticias.html', context)

def adminServicios(request):
    servicios = Servicio.objects.all()
    context = {'servicios': servicios}
    return render(request, 'crud/adminServicios.html', context)

def noticia(request):
    context = {'mensaje': 'OK, datos guardados con éxito'}
    return render(request, 'crud/servicio.html', context)