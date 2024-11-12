from django import forms
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from appAlumno.models import Alumno, Curso
from django.core.exceptions import ValidationError

class FormularioAlumno(forms.ModelForm):
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
        help_text="<p class='text-muted'>Ejemplo: Luis Henríquez</p>"
    )

    direccion = forms.CharField(
        max_length=50,
        validators=[RegexValidator(
            r'^[A-Za-z\s]+ #\d+$', 
            'La dirección debe tener el nombre de la calle, seguido de # y un número'
        )],
        help_text="<p class='text-muted'>Ejemplo: 11 de Septiembre #420</p>"
    )

    telefono = forms.CharField(
        max_length=9,
        validators=[RegexValidator(
            r'^9\d{8}$', 
            'El teléfono debe comenzar con 9 y tener 9 dígitos en total'
        )],
        help_text="<p class='text-muted'> Ejemplo: <strong>9</strong>50502430</p>"
    )
    
    edad = forms.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(120)],
        help_text= "<p class='text-muted'>Ingrese una edad entre 1 y 120</p>"
    )

    class Meta:
        model = Alumno
        fields = '__all__'

class FormularioCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['codigo', 'horas', 'nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'seccion', 'profesor']

    def vcodigo(self):
        codigo = self.cleaned_data.get('codigo')
        if not codigo.isalnum():
            raise ValidationError("El código debe contener letras y numeros.") #el codigo tiene que tener letras y numeros
        return codigo

    def vhoras(self):
        horas = self.cleaned_data.get('horas')
        if horas <= 0:
            raise ValidationError("Las horas deben ser mayores a 0.")  #horas tienen q ser mayor a 0
        return horas

    def vnombre(self):
        nombre = self.cleaned_data.get('nombre')  
        if not all(x.isalpha() or x.isspace() for x in nombre):
            raise ValidationError("El nombre debe contener solo letras y espacios.")   #tiene q tener letras y espacios gracias al metodo isalpha y isspace
        return nombre

    def vdescripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if not descripcion:
            raise ValidationError("La descripción no puede estar vacía.")  #la descripcion no debe estar vacia
        return descripcion

    def vseccion(self):
        seccion = self.cleaned_data.get('seccion')
        if not seccion.isalnum():
            raise ValidationError("La sección debe contener letras y numeros.") #la seccion tiene que contener letras y numeros
        return seccion
