from django.shortcuts import render,  get_object_or_404, redirect
import uuid
from .models import Servicio  

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



def modificarServicio(request, id_servicio):
    servicio = get_object_or_404(Servicio, id_servicio=id_servicio)
    
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        valor = request.POST.get("valor")
        telefono = request.POST.get("telefono")
        Email = request.POST.get("Email")
        imagen = request.FILES.get("imagen")
        
        servicio.titulo = titulo
        servicio.valor = valor
        servicio.telefono = telefono
        servicio.Email = Email
        if imagen:
            servicio.imagen = imagen
        
        servicio.save()
        
        return redirect('admin')
    
    context = {
        'servicio': servicio,
    }
    return render(request, 'crud/modificarServicio.html', context)


def eliminarServicio(request, id_servicio):
    servicio = get_object_or_404(Servicio, id_servicio=id_servicio)
    if request.method == "POST":
        servicio.delete()
        mensaje = "OK, datos eliminados satisfactoriamente"
        servicios = Servicio.objects.all()
        context = {'servicios': servicios, 'mensaje': mensaje}
        return render(request, 'crud/admin.html', context)
    else:
        context = {'servicio': servicio}
        return render(request, 'crud/eliminarServicio.html', context)



def admin_view(request):
    servicios = Servicio.objects.all()
    context = {'servicios': servicios}
    return render(request, 'crud/admin.html', context)
