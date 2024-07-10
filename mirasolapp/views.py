from django.shortcuts import render, redirect, get_object_or_404
import uuid
from .models import Servicio, Noticia
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    request.session["usuario"]="USUARIO"
    usuario =request.session["usuario"]
    context = {'usuario':usuario}
    return render(request,'mirasolapp/index.html', context)

@login_required
def login(request):
    context = {}
    return render(request, 'registration/login.html', context)

@login_required
def logout(request):
    context = {}
    return render(request, 'registration/logout.html', context)

def formulario(request):
    context = {}
    return render(request, 'mirasolapp/formulario.html', context)

def noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'mirasolapp/noticias.html', {'noticias': noticias})

@login_required
def vistaNoticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'crud/vistaNoticias.html', {'noticias': noticias})

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'mirasolapp/servicios.html', {'servicios': servicios})

@login_required
def seleccionVista(request):
    context = {}
    return render(request, 'crud/seleccionVista.html', context)

@login_required
def vistaServicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'crud/vistaServicios.html', {'servicios': servicios})

@login_required
def agregarNoticia(request):
    if request.method == "POST":
        titular = request.POST.get("titular")
        breve_desc = request.POST.get("breve_desc")
        noticia = request.POST.get("noticia")
        imagen = request.FILES.get("imagen")

        noticia = Noticia(
            titular=titular,
            breve_desc=breve_desc,
            noticia=noticia,
            imagen=imagen
        )

        noticia.save()

        context = {'mensaje': 'OK, datos guardados con éxito'}
        return render(request, 'crud/noticia.html', context)
    else:
        return render(request, 'crud/agregarNoticia.html')
 
@login_required   
def agregarServicio(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        valor = request.POST.get("valor")
        telefono = request.POST.get("telefono")
        Email = request.POST.get("Email")
        imagen = request.FILES.get("imagen")

        servicio = Servicio(
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
        return render(request, 'crud/agregarServicio.html')



@login_required
def modificarNoticia(request, id_noticia):
    noticia = get_object_or_404(Noticia, id_noticia=id_noticia)
    
    if request.method == 'POST':
        noticia.titular = request.POST['titular']
        noticia.breve_desc = request.POST['breve_desc']
        noticia.noticia = request.POST['noticia']
        
        if 'nueva_imagen' in request.FILES:
            noticia.imagen = request.FILES['nueva_imagen']
        
        noticia.save()
        return redirect('adminNoticias')  # Redirect to the admin page after saving changes
    
    return render(request, 'crud/modificarNoticia.html', {"noticia": noticia})



@login_required
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

@login_required
def eliminarServicio(request, id_servicio):
    servicio = get_object_or_404(Servicio, id_servicio=id_servicio)
    servicio.delete()

    return redirect('adminServicios') 

@login_required
def eliminarNoticia(request, id_noticia):
    noticia = get_object_or_404(Noticia, id_noticia=id_noticia)
    noticia.delete()

    return redirect('adminNoticias') 

@login_required
def adminNoticias(request):
    noticias = Noticia.objects.all()
    context = {'noticias': noticias}
    return render(request, 'crud/adminNoticias.html', context)

@login_required
def adminServicios(request):
    servicios = Servicio.objects.all()
    context = {'servicios': servicios}
    return render(request, 'crud/adminServicios.html', context)
