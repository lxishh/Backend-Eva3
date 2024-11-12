from django.db import models
from appProfesor.models import Profesor

# Create your models here.
class Alumno(models.Model):
    dni = models.CharField(max_length=10, unique=True)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    edad = models.PositiveIntegerField()

class Curso(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    horas = models.PositiveIntegerField()
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()    #antes programa
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    seccion = models.CharField(max_length=20) #antes numero
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def datos_curso(self):
        return "{}, {}".format(self.nombre, self.codigo)
    
    def __str__(self):
        return self.datos_curso()