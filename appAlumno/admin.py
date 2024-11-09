from django.contrib import admin
from appAlumno.models import Alumno
from appProfesor.models import Profesor

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['dni', 'direccion', 'telefono', 'edad']

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['dni', 'nombre', 'direccion', 'telefono']

# Register your models here.
admin.site.register(Alumno, AlumnoAdmin)

admin.site.register(Profesor, ProfesorAdmin)