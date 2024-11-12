from django.db import models
from appProfesor.models import Profesor
from django.core.exceptions import ValidationError


# Create your models here.
class Alumno(models.Model):
    dni = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=30, default="Desconocido")
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    edad = models.PositiveIntegerField()
    #relacion con curso:
    cursos = models.ManyToManyField("Curso", related_name="alumnos")

    def datos_alumno(self):
        return "{}, {}".format(self.nombre, self.dni)
    
    def __str__(self):
        return self.datos_alumno()

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