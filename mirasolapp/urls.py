from django.urls import path
from . import views

#Creamos una lista con URL

urlpatterns = [
    path('', views.index, name='index'),
    path('noticias', views.noticias, name='noticias'),
    path('servicios', views.servicios, name='servicios'),
    path('login', views.login, name='login'),
    path('formulario', views.formulario, name='formulario'),
]