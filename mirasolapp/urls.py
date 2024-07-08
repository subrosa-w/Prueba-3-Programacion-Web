from django.urls import path, include
from . import views

#Creamos una lista con URL

urlpatterns = [
    #!path del usuario
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('noticias', views.noticias, name='noticias'),
    path('servicios/', views.servicios, name='servicios'),
    path('formulario', views.formulario, name='formulario'),

    #?path del administrador
    path('adminServicios/', views.adminServicios, name='adminServicios'),
    path('modificarServicio/<id_servicio>', views.modificarServicio, name='modificarServicio'),
    path('eliminarServicio/<id_servicio>', views.eliminarServicio, name='eliminarServicio'),
    path('agregarServicio/', views.agregarServicio, name='agregarServicio'),
    path('vistaServicios/', views.vistaServicios, name='vistaServicios'),
    path('adminNoticias/', views.adminNoticias, name='adminNoticias'),
    path('modificarNoticia/<str:id_noticia>/', views.modificarNoticia, name='modificarNoticia'),
    path('eliminarNoticia/<str:id_noticia>', views.eliminarNoticia, name='eliminarNoticia'),
    path('agregarNoticia/', views.agregarNoticia, name='agregarNoticia'),
    path('vistaNoticias/', views.vistaNoticias, name='vistaNoticias'),
    path('seleccionVista/', views.seleccionVista, name='seleccionVista'),

    #SESSION
    path("accounts/", include("django.contrib.auth.urls")),
]


