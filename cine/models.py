from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Pelicula(models.Model):
    nombre = models.CharField(max_length=50)
    duracion = models.CharField(max_length=5)
    genero = models.CharField(max_length=20)
    director = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Cine(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Sala(models.Model):
    cine = models.ForeignKey(Cine, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)
    numeroAcientos = models.IntegerField()

    def __str__(self):
        return str(self.nombre + ' ' + self.cine.nombre)


class Funcion(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.PROTECT)
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)
    fecha = models.DateField(auto_now=False)
    valor = models.IntegerField()
    hora = models.DateTimeField(auto_now=False)

    def __str__(self):
        return str(self.sala.nombre + ' ' + self.pelicula.nombre)


class Usuario(AbstractUser):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=50)
    token = models.CharField(max_length=100, null=True, blank=True, default='')


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Boleta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    funcion = models.ForeignKey(Funcion, on_delete=models.PROTECT)
    asientos = models.CharField(max_length=50)
    valor = models.IntegerField()
