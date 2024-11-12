from django.contrib import admin
from appAlumno.models import Alumno, Curso
from appProfesor.models import Profesor

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['dni', 'direccion', 'telefono', 'edad']

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['dni', 'nombre', 'direccion', 'telefono']

class CursoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'horas', 'descripcion', 'fecha_inicio', 'fecha_fin', 'seccion', 'profesor']


# Register your models here.
admin.site.register(Alumno, AlumnoAdmin)

admin.site.register(Profesor, ProfesorAdmin)

admin.site.register(Curso, CursoAdmin)