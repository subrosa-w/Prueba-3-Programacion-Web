from django.db import models

# Create your models here.

class Servicio(models.Model):
    id_servicio = models.CharField(primary_key=True, max_length=10)
    imagen = models.ImageField(upload_to='servicios')
    titulo = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    telefono = models.CharField(max_length=10)
    Email = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo