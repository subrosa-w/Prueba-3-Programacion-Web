from django.db import models

# Create your models here.

class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='servicios')
    titulo = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=0)
    telefono = models.CharField(max_length=10)
    Email = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo
    
class Noticia(models.Model):
    id_noticia = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='noticias')
    titular = models.CharField(max_length=20)
    breve_desc = models.CharField(max_length=30)
    noticia = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titular