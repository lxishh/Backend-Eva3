from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Profesor(models.Model):
    dni = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=9)
    direccion = models.CharField(max_length=50)

    def datos_profesor(self):
        return "{}, {}".format(self.nombre, self.dni)
    
    def __str__(self):
        return self.datos_profesor()
    
    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        db_table = 'profesor'
        ordering = ['nombre']