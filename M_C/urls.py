#from django.config.urls import url
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='index'),
    path('login',views.login, name='login'),
    path('noticias',views.noticias, name='noticias'),
    path('servicios',views.servicios, name='servicios'),
    path('formulario',views.formulario, name='formulario'),
    
]