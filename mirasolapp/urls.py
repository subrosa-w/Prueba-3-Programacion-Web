from django.urls import path
from . import views

#Creamos una lista con URL

urlpatterns = [
    path('index', views.index, name='index'),
    path('noticias', views.noticias, name='noticias'),
    path('servicios', views.servicios, name='servicios'),
    path('', views.login, name='login'),
    path('formulario', views.formulario, name='formulario'),
]