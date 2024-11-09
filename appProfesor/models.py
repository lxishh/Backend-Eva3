from django.db import models
from django.core.exceptions import ValidationError

def validnombre(value):
    if any(vnombre.isdigit() for vnombre in value):
        raise ValidationError('el nombre no puede tener numeros.')

def validnumeros(value):
    if not value.isdigit() or int(value) <0:
        raise ValidationError('no puede tener numeros negativos/letras este campo')

# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=30,validators=[validnombre])
    telefono = models.CharField(max_length=30,validators=[validnumeros])
    dni = models.CharField(max_length=30,validators=[validnumeros])
    direccion = models.CharField(max_length=30)


    