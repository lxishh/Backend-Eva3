from django import forms
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from appProfesor.models import Profesor


def validar_edad(valor):
    if valor <= 0:
        raise ValidationError('La edad debe ser un número positivo.')
    elif valor > 120:
        raise ValidationError('La edad no es válida.')

class FormProfesor(forms.ModelForm):
    dni = forms.CharField(
        max_length=10,
        validators=[RegexValidator(
            r'^\d{8}-[0-9A-Za-z]$',
            'El DNI debe tener 8 dígitos, un guion y un número o letra al final'
        )],
        help_text="<p class='text-muted'>Ejemplo: 12345678-K o 12345678-1</p>"
    )

    nombre = forms.CharField(
        max_length=30,
        validators=[RegexValidator(
            r'^[A-Za-z\s]+$',
            'El nombre debe contener solo letras y espacios'
        )],
        help_text="<p class='text-muted'>Ejemplo: Juan Pérez</p>"
    )

    direccion = forms.CharField(
        max_length=50,
        validators=[RegexValidator(
            r'^[A-Za-z\s]+ #\d+$',
            'La dirección debe tener el nombre de la calle, seguido de # y un número'
        )],
        help_text="<p class='text-muted'>Ejemplo: Avenida Siempre Viva #742</p>"
    )

    telefono = forms.CharField(
        max_length=9,
        validators=[RegexValidator(
            r'^9\d{8}$',
            'El teléfono debe comenzar con 9 y tener 9 dígitos en total'
        )],
        help_text="<p class='text-muted'>Ejemplo: <strong>9</strong>87654321</p>"
    )

    edad = forms.IntegerField(
        validators=[validar_edad],
        help_text="<p class='text-muted'>Ingrese una edad razonable entre 1 y 120 años.</p>"
    )

    class Meta:
        model = Profesor
        fields = '__all__'

