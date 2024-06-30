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
    servicios = Servicio.objects.all()
    return render(request, 'mirasolapp/servicios.html', {'servicios': servicios})

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
    
    if request.method == 'POST':
        servicio.titulo = request.POST['titulo']
        servicio.valor = request.POST['valor']
        servicio.telefono = request.POST['telefono']
        servicio.Email = request.POST['Email']
        
        if 'nueva_imagen' in request.FILES:
            servicio.imagen = request.FILES['nueva_imagen']
        
        servicio.save()
        return redirect('admin')  # Redirige a la página de administración después de guardar los cambios
    
    return render(request, 'crud/modificarServicio.html', {"servicio": servicio})

def eliminarServicio(request, id_servicio):
    servicio = get_object_or_404(Servicio, id_servicio=id_servicio)
    servicio.delete()

    return redirect('admin') 

def eliminarServicio(request, id_servicio):
    servicio = get_object_or_404(Servicio,id_servicio=id_servicio)
    servicio.delete()

    return redirect('admin')

def admin_view(request):
    servicios = Servicio.objects.all()
    context = {'servicios': servicios}
    return render(request, 'crud/admin.html', context)
