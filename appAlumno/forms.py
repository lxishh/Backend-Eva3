from django import forms
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from appAlumno.models import Alumno

class FormularioAlumno(forms.ModelForm):
    dni = forms.CharField(
        max_length=10,
        validators=[RegexValidator(
            r'^\d{8}-[0-9A-Za-z]$', 
            'El DNI debe tener 8 dígitos, un guion y un número o letra al final'
        )],
        help_text="<p class='text-muted'>Ejemplo: 12345678-K o 12345678-1</p>"
    )

    direccion = forms.CharField(
        max_length=50,
        validators=[RegexValidator(
            r'^[A-Za-z\s]+ #\d+$', 
            'La dirección debe tener el nombre de la calle, seguido de # y un número'
        )],
        help_text="<p class='text-muted'>Ejemplo: Ramon Carnicer #2003</p>"
    )

    telefono = forms.CharField(
        max_length=9,
        validators=[RegexValidator(
            r'^9\d{8}$', 
            'El teléfono debe comenzar con 9 y tener 9 dígitos en total'
        )],
        help_text="<p class='text-muted'> Ejemplo: <strong>9</strong>50501230</p>"
    )
    
    edad = forms.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(120)],
        help_text= "<p class='text-muted'>Ingrese una edad entre 1 y 120</p>"
    )

    class Meta:
        model = Alumno
        fields = '__all__'
