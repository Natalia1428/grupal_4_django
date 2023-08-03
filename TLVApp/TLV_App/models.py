from django.db import models
from django.contrib.auth.models  import User

#importar reverse
from django.shortcuts import reverse

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    edad = models.IntegerField()
    hobby = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('cliente')
    
    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()