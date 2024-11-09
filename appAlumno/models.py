from django.db import models

# Create your models here.
class Alumno(models.Model):
    dni = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    edad = models.IntegerField()
