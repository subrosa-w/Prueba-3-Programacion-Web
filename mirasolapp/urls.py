from django.urls import path
from . import views

#Creamos una lista con URL

urlpatterns = [
    #!path del usuario
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('noticias', views.noticias, name='noticias'),
    path('servicios/', views.servicios, name='servicios'),
    path('formulario', views.formulario, name='formulario'),

    #?path del admin
    path('admin/', views.admin_view, name='admin'),
    path('modificarServicio/<id_servicio>', views.modificarServicio, name='modificarServicio'),
    path('eliminarServicio/<id_servicio>', views.eliminarServicio, name='eliminarServicio'),
    path('agregarServicio/', views.agregarServicio, name='agregarServicio'),
    path('seleccionVista/', views.seleccionVista, name='seleccionVista'),
    path('vistaServicios/', views.vistaServicios, name='vistaServicios'),
]

